from django.conf.urls import url

from massadv import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^top/$', views.top, name='top'),
    url(r'^left/$', views.left, name='left'),
    url(r'^main/$', views.main, name='main'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^sell/$', views.sell, name='sell'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^images/$', views.images, name='images'),
    url(r'^category/(\d{1,5})$', views.category, name='category'),
    url(r'^items/$', views.items, name='items'),
    url(r'^details/$', views.details, name='details'),
    url(r'^register/$', views.details, name='details'),
    url(r'^manage/$', views.manage, name='manage'),
    url(r'^settings/$', views.settings, name='settings'),
]

