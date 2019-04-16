from django.db import models

# Create your models here.

class BookInfo(models.Model):
    bname = models.CharField(max_length=20)
    bpub_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bname

class Hero(models.Model):
    hname = models.CharField(max_length=20)
    bsex = models.BooleanField()
    bfrom_bid = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname



