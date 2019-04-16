from django.contrib import admin
from .models import BookInfo,Hero

# Register your models here.
admin.site.register(Hero)
admin.site.register(BookInfo)