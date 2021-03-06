# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TengxuncrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	zhName = scrapy.Field()
    # 链接
	zhLink = scrapy.Field()
    # 类别
	zhType = scrapy.Field()
    # 人数
	zhNum = scrapy.Field()
    # 地点
	zhAddress = scrapy.Field()
    # 发布时间
	zhTime = scrapy.Field()

