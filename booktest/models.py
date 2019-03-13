from django.db import models

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False, default=0)
    isDelete = models.BooleanField(default=False) #逻辑删除
    def __str__(self):
        return self.btitle
    class Meta:
        db_table = 'bookinfo'

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontant = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE) #外键。需要加on_deiete选项
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname



