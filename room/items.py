# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RoomItem(scrapy.Item):
    title=scrapy.Field()
    station=scrapy.Field()
    price=scrapy.Field()
    info=scrapy.Field()
    img=scrapy.Field()
    phone=scrapy.Field()

