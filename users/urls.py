#coding=gbk
from django.urls import re_path
from django.contrib.auth.views import login

from . import views

app_name='users'

urlpatterns=[
    # 登录页面
    re_path(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
    
    # 注销页面
    re_path(r'^logout/$',views.logout_view,name='logout'),
    
    # 用户注册页面
    re_path(r'^register/$',views.register,name='register'),
]
