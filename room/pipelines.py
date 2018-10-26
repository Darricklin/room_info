# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

import pymysql
import redis
class MysqlPipeline(object):
    def open_spider(self,spider):
        self.connect=pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='s19930110l',
            db='u148'
        )
        self.cursor=self.connect.cursor()
    def process_item(self,item,spider):
        sql='insert into room values(0,"%s","%s","%s","%s","%s","%s")'%(item['title'],item['station'],item['price'],item['info'],item['img'],item['phone'])
        self.cursor.execute(sql)
        self.connect.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()

class RoomPipeline(object):
    def open_spider(self,spider):
        self.fileobj=open('room.csv','w',encoding='utf-8')
        self.csv=csv.writer(self.fileobj)
        self.csv.writerow(['title','station','price','info','img','phone'])
        self.item_list=[]
    def process_item(self,item,spider):
        childcsv=[]
        childcsv.append(item['title'])
        childcsv.append(item['station'])
        childcsv.append(item['price'])
        childcsv.append(item['info'])
        childcsv.append(item['img'])
        childcsv.append(item['phone'])
        self.item_list.append(childcsv)
        return item
    def close_spider(self,spider):
        self.csv.writerows(self.item_list)
        self.fileobj.close()