from django.shortcuts import render
import os
# Create your views here.


def index(request):
	return render(request, 'CustomData/index.html')


def search(request):

	 os.system("scrapy crawl webtitlescrapy")
	 
	 return render(request, 'CustomData/index.html', context)
