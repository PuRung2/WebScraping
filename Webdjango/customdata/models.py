from django.db import models

# Create your models here.

class ExampleDotCom(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title



class NewsUrl(models.Model):

	newraddress = models.TextField(max_length=255)