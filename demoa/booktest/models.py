from django.db import models

# Create your models here.

class BookInfo(models.Model):
    bname = models.CharField(max_length=20)
    bpub_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bname

    def disname(self):
        return self.bname
    disname.short_description = '书名'

    def destime(self):
        return self.bpub_time
    destime.short_description = '发布时间'


class Hero(models.Model):
    hname = models.CharField(max_length=20)
    hsex = models.BooleanField()
    bid = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname
