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
    # # 渲染模板
    # indextem = loader.get_template('booktset/index.html')
    # # 添加动态数据到模板（必须是字典类型）
    # dyn = indextem.render({'user': 'bh'})
    # # 返回模板
    # return HttpResponse(dyn)
    return render(request, 'booktset/index.html', {'user': 'bh'})



def showlist(request):
    # return HttpResponse("展示列表")
    booklist = BookInfo.objects.all()
    return render(request, 'booktset/list.html', {'booklist': booklist})

# 传参
def detail(request, id):
    # try:
    #     print(id, type(id))
    #     b = BookInfo.objects.get(pk=int(id))
    #     return HttpResponse("白落梅：" + b.bname)
    # except:
    #     print('没有这本书')
    book = BookInfo.objects.get(pk= int(id))
    heroset = book.hero_set.all()
    # 参数：1，请求，不用管；2.模板名称，第一级目录在settings以后的需要在此处模板子目录写起,3.参数字典
    return render(request, 'booktset/detail.html', {'heroset': heroset})
