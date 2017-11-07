from django.conf.urls import url
from . import views

app_name = "project"

urlpatterns = [
    url(r'^wishlist$', views.wishlist, name="wishlist"),
    url(r'^additem', views.additem, name="additem"),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^itemadded/(?P<id>\d+)$', views.itemadded, name='itemadded'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),
    url(r'^iteminfo/(?P<id>\d+)$', views.iteminfo, name='iteminfo'),
    url(r'^add2wish/(?P<id>\d+)$', views.add2wish, name='add2wish'),
]
