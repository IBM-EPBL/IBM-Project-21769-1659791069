from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login', views.loginpage, name='login'),
    path('logout/', views.logoutusers, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('products/', views.services, name='services'),
    path('index/', views.index, name='index'),
    path('quoteform/', views.quote, name='quote'),
    path('', views.landing_page, name='landingpage'),

]

