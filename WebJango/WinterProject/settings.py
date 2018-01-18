# -*- coding: utf-8 -*-
import os
import sys

DJANGO_PROJECT_PATH = '.'
DJANGO_SETTINGS_MODULE = 'example_project.settings'

sys.path.insert(0, DJANGO_PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE
BOT_NAME = 'example_bot'

SPIDER_MODULES = ['example_bot.spiders']



BOT_NAME = 'WinterProject'
 
SPIDER_MODULES = ['WinterProject.spiders']
NEWSPIDER_MODULE = 'WinterProject.spiders'
LOG_LEVEL='ERROR'
#
# Url 크롤링시 CSVPipeline 설정
ITEM_PIPELINES = {'WinterProject.pipelines.CsvPipeline':300,
  'example_bot.pipelines.ExPipeline': 1000, }
 
# 기사 내용 크롤링시 MongoDBPipeline 설정
#ITEM_PIPELINES = {'newscrawling.pipelines.MongoDBPipeline': 300,}
 
#MONGODB_SERVER = "localhost"
#MONGODB_PORT = 27017
#MONGODB_DB = "news_crawl"
#MONGODB_COLLECTION = "news"


