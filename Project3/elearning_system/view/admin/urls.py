from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^manageTopic', views.manageTopic, name='admin'),
    url(r'^manageUser', views.manageUser, name='manageUser'),
    url(r'^manageModerator', views.manageModerator, name='manageModerator'),
    url(r'^change_status_user', views.change_status_user, name='change_status_user'),
]
