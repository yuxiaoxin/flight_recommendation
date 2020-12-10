"""Demo URL Configuration

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
from django.conf.urls import url
from web import views

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # 第一个参数是url，第二个参数是输入前面的url调用views里的方法
    url(r'^admin/', admin.site.urls),  # admin后台路由
    # 网址入口，关联到对应的views.py中的一个函数
    url(r'^flightPie/', views.flightPie),
    url(r'^airportAccount/', views.airportAccount),
    url(r'^airportNumber/', views.airportNumber),
    url(r'^geoLine/', views.geoLine),
    url(r'^404/', views.wrong),
    url(r'^quireFault/', views.wrong2),
    url(r'^airport/', views.airport),
    url(r'^discount/', views.discount),
    url(r'^priceShow/', views.priceShow),
    url(r'^newLogin/', views.newLogin),
    url(r'^airportDiscount/', views.airportDiscount),
    url(r'^airportPunctual/', views.airportPunctual),
    url(r'^airportRecommend/', views.airportRecommend),
    url(r'^register/', views.register),
    url(r'^flightLine/', views.flightLine),

]
