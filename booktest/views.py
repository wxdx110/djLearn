from django.shortcuts import render
from .models import *
from django.http import *
from django.conf import settings
import os
# from django.template import RequestContext, loader
def base(request):
    return render(request, 'booktest/base.html')
def index(request):
    # temp = loader.get_template('booktest/index.html') #加载页面
    # red = temp.render() # 渲染页面
    # return HttpResponse(red)
    bookList = BookInfo.books.all() #books是自己写的管理器，显示未逻辑删除的对象
    context = {'list':bookList}
    return render(request, 'booktest/index.html', context)
def show(request, id):
    book = BookInfo.books.get(pk = id)
    heroList = book.heroinfo_set.all()
    context = {'list': heroList}
    return render(request, 'booktest/show.html',context)
def getTest(request):
    return render(request, 'booktest/getTest.html')
def getTest1(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    contest = {'a':a, 'b':b, 'c':c}
    return render(request, 'booktest/getTest1.html',contest)

def postTest1(request):
    return render(request, 'booktest/postTest1.html')
def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname, 'upwd':upwd, 'ugender':ugender, 'uhobby':uhobby}
    return render(request, 'booktest/postTest2.html', context)
def picTest(request):
    return render(request, 'booktest/picTest.html')
def picHandle(request):
    if request.method == "POST":
        f1 = request.FILES['pic1']
        # fname = r'%s/%s' % (settings.MEDIA_ROOT, f1.name)
        fname = os.path.join(settings.MEDIA_ROOT, f1.name)
        with open(fname, 'wb+') as pic:
            for c in f1.chunks():
                pic.write(c)
        return HttpResponse('<img src="/static/booktest/media/%s">'%f1.name)
    else:
        return HttpResponse("error")
