from django.conf.urls import url
from . import views
# 添加应用名
app_name = 'vote'
# 子级请求
urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^del/(\d+)/$', views.detail, name='detail'),
    url(r'^ckfs/$', views.score, name='ckfs')
]