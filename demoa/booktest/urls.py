from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

# 应用下的第二级请求路径

urlpatterns = [
    # 子级请求要求：r
    #                 ^
    #                     $
    url(r'idx/$', views.index),
    url(r'l/$', views.showlist),
    # 请求传参：/后使用正则表示参数格式如整数:\d
    url(r'^det/(\d+)/$', views.detail),
]
