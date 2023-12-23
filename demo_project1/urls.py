"""
URL configuration for demo_project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from firstapp import views

admin.site.site_header="anil Admin"
admin.site.site_title="anil portal"
admin.site.index_title="Welcome to Anil's activities performed"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',views.fun),
    path('home/',views.launch),
    path('home/success/',views.success),
    path('services/',views.services),
    path('about/',views.about),
    path('contact/',views.contact, name='contact'),
    path('web2/',views.web2, name='web2'),
    path('web2/zomato/',views.zomato, name='zomato'),  
]
