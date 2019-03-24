import requests
from bs4 import BeautifulSoup

base_url = "https://search.jd.com/Search?keyword="
keywords = ['iphone', '衣服', '鞋子', '童装', '零食', '眼镜']
list = []
headers = {
    'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML, like Gecko)\
    chrome//52.0.2743.116 Safari/537.36'
    }
zyt = []
zsw = []
lz = []


for keyword in keywords:
    for i in range(10):
        response = requests.get(base_url + '%s&page=%s&enc=utf-8'%(keyword, 2 * i + 1), headers = headers)
        response.encoding = 'UTF-8'
        bp = BeautifulSoup(response.text, 'lxml')
        for item in bp.find_all('li', {'class':'gl-item'}):
            list.append('https://item.jd.com/' + item.get('data-sku') + '.html#comment')
for i in range(600):
    zyt.append(list[i])
for i in range(601, 1200):
    zsw.append(list[i])
try:
    for i in range(1201, 1800):
        lz.append(list[i])
except:
    pass
    
    
