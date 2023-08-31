from django.db import models
from django.shortcuts import render

# 1 Question
class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)




# 2 question
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

products = Product.objects.all()