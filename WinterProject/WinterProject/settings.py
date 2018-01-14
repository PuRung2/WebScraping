# -*- coding: utf-8 -*-

BOT_NAME = 'WinterProject'
 
SPIDER_MODULES = ['WinterProject.spiders']
NEWSPIDER_MODULE = 'WinterProject.spiders'
LOG_LEVEL='ERROR'
#
# Url 크롤링시 CSVPipeline 설정
ITEM_PIPELINES = {'WinterProject.pipelines.CsvPipeline':300 }
 
# 기사 내용 크롤링시 MongoDBPipeline 설정
#ITEM_PIPELINES = {'newscrawling.pipelines.MongoDBPipeline': 300,}
 
#MONGODB_SERVER = "localhost"
#MONGODB_PORT = 27017
#MONGODB_DB = "news_crawl"
#MONGODB_COLLECTION = "news"


