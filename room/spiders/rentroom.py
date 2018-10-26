# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from room.items import RoomItem
import re

class RentroomSpider(CrawlSpider):
    name = 'rentroom'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/zufang']
    rules = (
        Rule(LinkExtractor(allow='/zufang/pg\d+/'), callback='parse_item'),
    )
    def parse_item(self, response):
        room_list=response.xpath("//div[@class='list-wrap']//li")
        for room in room_list:
            item=RoomItem()
            item['title']=room.xpath(".//h2/a/text()").extract()[0]
            item['station'] =''.join(re.findall('(\w+)',room.xpath(".//div[@class='where']//span/text()").extract()[0]))
            item['price'] = room.xpath(".//div[@class='price']//text()").extract()[0]+'元/月'
            next_url=room.xpath(".//h2/a/@href").extract()[0]
            yield scrapy.Request(url=next_url,callback=self.parse_next,meta={'item':item})
    def parse_next(self,response):
        item=response.meta['item']
        item['img']=response.xpath("//div[@class='thumbnail']//li/@data-src").extract()
        item['info'] =''.join(re.findall('\w',''.join(response.xpath("//div[@class='featureContent']//li//text()").extract())))
        item['phone'] =''.join(re.findall('\d',''.join(response.xpath(".//div[@class='brokerInfoText']/div[@class='phone']//text()").extract())))
        yield item

