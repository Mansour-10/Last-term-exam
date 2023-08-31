from django.urls import path
from . import views



urlpatterns =[
    path('', views.master, name="master"),
    path('products/', views.product_list, name='product_list'),

]


