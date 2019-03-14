from django.db import models

class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False) #只显示未逻辑删除的
    def create(self, title, date):
        b = BookInfo()
        b.btitle = title
        b.bpub_date = date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b
    # 建立对象：
    #     b = BookInfo.books.create('111',datetime(2019,1,1))
    #     b.save()

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False, default=0)
    isDelete = models.BooleanField(default=False) #逻辑删除
    def __str__(self):
        return self.btitle
    class Meta:
        db_table = 'bookinfo' #数据库生产表名
    books = BookInfoManager()

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE) #外键。需要加on_deiete选项
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname



