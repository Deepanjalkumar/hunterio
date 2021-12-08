"""hunterio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name="home"),
    path('domain_search', views.domain_search, name="domain_search"),
    path('email_finder', views.email_finder, name="email_finder"),
    path('author_finder', views.author_finder, name="author_finder"),
    path('email_verifier', views.email_verifier, name="email_verifier"),  
    path('pricing', views.pricing, name="pricing"),
    path('blog', views.blog, name="blog"),
    path('templa', views.templa, name="templa"),
    path('help_center', views.help_center, name="help_center"),
    path('about_us', views.about_us, name="about_us"),
    path('our_data', views.our_data, name="our_data"),
    path('careers', views.careers, name="careers"),
    path('loginuser', views.loginuser, name="loginuser"),
    
    
    
    
    
        
]
