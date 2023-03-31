from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=300)
    def __str__(self):
        return self.title

class Tags(models.Model):
    title=models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Image(models.Model):
    image=models.ImageField(upload_to='media/')

class Blog(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tags)
    image=models.ManyToManyField(Image)
    created_at=models.DateField('date published')

    def __str__(self):
        return self.title