"""webserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from cmdb import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^login', views.login),
    url(r'^home', views.home),
    url(r'^orm', views.orm),
    url(r'^userinfo', views.userinfo),
    url(r'^groupinfo', views.groupinfo),
    url(r'^hostinfo', views.hostinfo),
    url(r'^idcinfo', views.idcinfo),
    url(r'^userdetail-(?P<nid>\d+)/', views.userdetail),
    url(r'^userdel-(?P<nid>\d+)/', views.userdel),
    url(r'^useredit-(?P<nid>\d+)/', views.useredit),
    url(r'^hostdetail-(?P<nid>\d+)/', views.hostdetail),
    url(r'^hostedit-(?P<nid>\d+)/', views.hostedit),
    url(r'^hostdel-(?P<nid>\d+)/', views.hostdel),

]
