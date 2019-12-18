"""LabrWorkPr URL Configuration

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
from django.conf.urls import url 
from django.urls import path
from CRUD_app import views

app_name = 'CRUD_app'  

urlpatterns = [
    
    url(r'^socialNetworks$', views.socialNetworks_list, name='socialNetworks_list'), 
    url(r'^new$', views.socialNetworks_create, name='socialNetworks_new'),  
    url(r'^edit/(?P<pk>\d+)$', views.socialNetworks_update, name='socialNetworks_edit'),  
    url(r'^delete/(?P<pk>\d+)$', views.socialNetworks_delete, name='socialNetworks_delete'),   
    url(r'^$', views.home_page_cn), 
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    
]
