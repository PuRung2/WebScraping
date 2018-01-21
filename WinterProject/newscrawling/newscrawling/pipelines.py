# -*- coding: utf-8 -*-
 
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from __future__ import unicode_literals
from scrapy.exporters import JsonItemExporter, CsvItemExporter
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
 

 
 
#JSON파일로 저장하는 클래스
class JsonPipeline(object):
    def __init__(self):
        self.file = open("newsCrawl.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='euc-kr', ensure_ascii=False)
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
 
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
 
#CSV 파일로 저장하는 클래스
class CsvPipeline(object):
    def __init__(self):
        self.file = open("newsUrlCrawl.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='euc-kr')
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
 
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
 


