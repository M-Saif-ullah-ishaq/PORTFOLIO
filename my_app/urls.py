"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from my_app import views 
# urls.py







urlpatterns = [
   
     path('',views.index,name="index" ),
     path('home',views.home,name="home" ),
     path('login',views.components,name="components" ),
     path('contact/', views.contact_view, name='contact_view'),
    #  path('success/', views.success_view, name='success_page'),

    

    #  path('logout',views.logout,name="logout" ),
]
