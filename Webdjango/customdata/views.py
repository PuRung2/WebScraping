from django.shortcuts import render
from .models import NewsUrl
import csv
 
def getCsv(request):

	csvList = []
	
	f = open('newsUrlCrawl.csv','r')    #현재 경로의 exam.csv를 연다.
	csvReader = csv.reader(f)    #reader로 파일을 읽는다.
	for i in csvReader:            #한 행씩 돌면서 i[2]값 (3번째 컬럼)을 가져와서 리스트에 저장한다.
		csvList.append(i)
		print(i.length())

	for cs in csvList:
		newsurl = NewsUrl(
    		newraddress = cs
    		)
		newsurl.save()

	f.close()

	return render(request, 'customdata/text.html')


def index(request):
	return render(request, 'customdata/index.html')