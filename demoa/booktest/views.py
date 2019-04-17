from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from django.template import loader

# Create your views here.
# 该应用下的视图函数


def index(request):
    """
    处理请求的函数，返回响应
    :param request: 请求，此参数时必须的
    :return: 相应内容
    """
    # return HttpResponse("这是首页!")
    # 渲染模板
    indextem = loader.get_template('booktset/index.html')
    # 添加动态数据到模板（必须是字典类型）
    dyn = indextem.render({'user': 'bh'})
    # 返回模板
    return HttpResponse(dyn)



def showlist(request):
    return HttpResponse("展示列表")


# 传参
def detail(request, id):
    try:
        print(id, type(id))
        b = BookInfo.objects.get(pk=int(id))
        return HttpResponse("白落梅：" + b.bname)
    except:
        print('没有这本书')
