from django.conf.urls import url
from django.contrib import admin
from rip_app import views


urlpatterns = (
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', views.index, name='index'),
    url(r'^best_members/', views.best_members, name='best_members'),
    url(r'^member/(?P<id>\d+)/?$', views.member, name='members'),
)
