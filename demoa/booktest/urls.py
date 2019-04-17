from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = "booktest"

# 应用下的第二级请求路径

urlpatterns = [
    # 子级请求要求：r
    #                 ^以...开头
    #                     $以...结尾
    url(r'^idx/$', views.index, name='index'),
    url(r'^l/$', views.showlist, name='list'),
    # 请求传参：/后使用正则表示参数格式如整数:\d
    url(r'^det/(\d+)/$', views.detail, name='detail'),
]
