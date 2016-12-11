

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list_ex$', views.list_ex_of_topic, name='list_ex'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^search$', views.search, name='search'),
]
