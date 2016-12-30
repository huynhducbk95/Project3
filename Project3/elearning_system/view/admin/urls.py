from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^manageTopic', views.manageTopic, name='manageTopic'),
    url(r'^manageUser', views.manageUser, name='manageUser'),
    url(r'^manageModerator', views.manageModerator, name='manageModerator'),
    url(r'^change_status_user', views.change_status_user, name='change_status_user'),
    url(r'^delete_moderator', views.delete_moderator, name='delete_moderator'),
]
