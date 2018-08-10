#coding=gbk
"""����blogs��URLģʽ"""

from django.urls import path,re_path

from . import views

app_name='blogs'

urlpatterns=[
    # ��ҳ
    re_path('posts',views.index,name='index'),
    re_path(r'^new_post/$',views.new_post,name='new_post'),
    re_path(r'^edit_post/(?P<post_id>\d+)/$',views.edit_post,name='edit_post'),
]
