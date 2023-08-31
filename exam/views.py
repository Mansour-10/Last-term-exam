from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost
from django.views.generic import ListView
from .models import Product


# 1
def mainpage(request):
    template = loader.get_template("master.html")
    return HttpResponse(template.render())

def blog_post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'master.html', {'posts': posts})


# 2
def x(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return x(n-1) + x(n-2)

n = int(input("Enter a number: "))
print(x(n))


# 3


class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'