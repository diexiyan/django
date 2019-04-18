from django.conf.urls import url

from .views import showpoet, index
# 【命名空间的使用解决url重构后超链接无法使用的问题】：在超链接中使用命名空间进行跳转
# 【1.】添加在应用下url下
app_name = 'item'

# 3.配置三级目录，二级请求：根据匹配到的网址找到对应的处理函数
# 注意，此处需要使用“r”原意；^，以……开始，$,以……结尾
# views.showpoet,视图函数的地址
urlpatterns = [
    # 添加name
    url(r'^p/$', showpoet, name='showpoet'),
    url(r'^$', index, name='index'),
]