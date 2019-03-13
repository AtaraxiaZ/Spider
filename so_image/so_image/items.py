# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
class ImageItem(Item):
    #连等式，即table和collection都是images
    #table表示mysql存储的表名称，collection表示mongodb存储的集合名
    collection = table = 'images'
    id = Field()
    url = Field()
    title = Field()
    thumb = Field()


