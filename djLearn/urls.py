"""djLearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import *
from booktest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('booktest/',include('booktest.urls')),
    # re_path(r'^(\d+)$', views.show)
    path('<int:id>/', views.show) #int类型的id
]
'''
path参数类型：
捕获url中的参数需要用到尖括号<> 指定尖括号中的值类型，这个转换器还有许多类型比如：
int 匹配0和正整数
str 匹配任何空字符串但不包括/
slug 可理解为注释 匹配任何ascii码包括连接线和下划线
uuid 匹配一个uuid对象（该对象必须包括破折号—，所有字母必须小写）
path 匹配所有的字符串 包括/（意思就是path前边和后边的所有）

'''