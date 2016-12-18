from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^errorMessage', views.errorMessage, name='errorMessage'),
    url(r'^messageDetail', views.messageDetail, name='messageDetail'),
    url(r'^exApproved', views.exApproved, name='exApproved'),
    url(r'^exUnapprove', views.exUnapprove, name='exUnapprove'),
    url(r'^exNoTopic', views.exNoTopic, name='exNoTopic'),
    url(r'^viewExUnapprove_detail', views.viewExUnapprove_detail, name='viewExUnapprove_detail'),
]
