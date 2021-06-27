"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from FirstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('h2/',views.h2tag),
    path('usr/<str:uname>/',views.welcomeUser),
    path('usr/<str:uname>/<int:uno>/',views.welcomeUser2),
    path('re/',views.htm),
    path('na/<str:uname>/',views.name),
    path('pt/<int:id>/<str:ename>',views.ename),
    path('form/',views.form),
    path('alert/',views.alert),
    path('myform/',views.myform,name='myform1'),
    path('bstreg/',views.bstreg),
    path('boot/',views.bootstrap),
    path('register1/',views.register1),
    path('register2/',views.register2,name='register2'),
    path('display1/',views.display1,name='display1'),
    path('view/<int:y>/',views.sview,name='sv'),
    path('update/<int:y>/',views.sup,name='sup'),

]
