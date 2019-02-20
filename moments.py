import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from time import sleep
from processor import Processor
from config import *


class Moments():
    def __init__(self):
        #初始化，驱动配置，延时等待配置，MongoDB配置
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity':APP_ACTIVITY
            }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]
        #处理时间，先要创建一个对象
        self.processor = Processor()
        
    def login(self):
        #登录按钮
        login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/e4g')))
        login.click()
        #手机输入
        phone = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/kh')))
        phone.set_text(USERNAME)
        #下一步
        next = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/axt')))
        next.click()
        #密码，因为上面的手机号的id也是kh，用列表中的第1个，手机号的其实是第0个，因为用//*返回的是一个列表
        password = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/kh"][1]')))
        password.set_text(PASSWORD)
        #提交
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/axt')))
        submit.click()
        #不调用通讯录
        address = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/az9')))
        address.click()
                                                           
                                                           

    def enter(self):
        #选项卡，因为“微信”“通讯录”“发现”“我”的id都是一样的，所以再添加一个参数instance
        tab = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/r4" and @instance="6"]')))
        tab.click()
        #朋友圈，只有点头像才有id，边上没有
        moments = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/akm')))
        moments.click()

    def crawl(self):
        while True:
            items = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[@resource-id="com.tencent.mm:id/cve"]//android.wiget.FrameLayout')))
             #上滑
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)

        for item in items:
            try:
                #昵称
                nickname = item.find_element_by_id('com.tencent.mm:id/b5o').get_attribute('text')
                #正文
                content = item.find_element_by_id('com.tencent.mm:id/kt').get_attribute('text')
                #日期
                date = item.find_element_by_id('com.tencent.mm:id/eec').get_attribute('text')
                #处理日期
                date = self.processor.date(date)
                print(nickname, content, date)
                data = {
                    'nickname':nickname,
                    'content':content,
                    'date':date,
                    }
                #插入MongoDB，使用$set表示，第一个参数的字典表示查询原条件，如果不存在就创建一个新的
                #如果有符合nickname和content的就看能否更新
                self.collection.update = ({'nickname':nickname, 'content':content}, {'$set':data}, True)
                sleep(SCROLL_SLEEP_TIME)
            except NoSuchElementException:
                pass

    def main(self):
        #登录
        self.login()
        #进入朋友圈
        self.enter()
        #爬取
        self.crawl()

if __name__ == '__main__':
    moments = Moments()
    moments.main()
