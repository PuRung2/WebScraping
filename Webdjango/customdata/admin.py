from django.contrib import admin

# Register your models here.
from .models import ExampleDotCom, NewsUrl

admin.site.register(ExampleDotCom)
admin.site.register(NewsUrl)