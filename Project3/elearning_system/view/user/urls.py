from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list_ex$', views.list_ex_of_topic, name='list_ex'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^search$', views.search, name='search'),
    url(r'^compare_exercise', views.compare_exercise, name='compare_exercise'),
    url(r'^login', views.login, name='login'),
    url(r'^registry', views.registry, name='registry'),
    url(r'^logout', views.logout, name='logout'),
]
