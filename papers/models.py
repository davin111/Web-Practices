from django.db import models

# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    abstract = models.TextField(max_length=3000)
    keywords = models.CharField(max_length=100)
    references = models.TextField(max_length=1000)