from django.contrib import admin
from .models import BookInfo,Hero

# Register your models here.
# 关联注册:1.创建类
class HeroInline(admin.StackedInline):
    # 被管理的类
    model = Hero
    # 添加的角色个数
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'disname', 'destime', ]
    search_fields = ['bname', 'bpub_time', ]

    # 关联注册2.添加到管理类
    inlines = [HeroInline, ]


class HeroAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hsex', 'bid', ]
    # 值为每页显示的条数
    list_per_page = 3


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(Hero, HeroAdmin)

