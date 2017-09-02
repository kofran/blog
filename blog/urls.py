from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from blog import views as signup
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^category/(?P<category>\w+)/$', views.category, name='category'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/profile/$', views.home, name='home'),
    url(r'^signup/$', signup.signup, name='signup'),
]
