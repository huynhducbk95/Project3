from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^errorMessage', views.errorMessage, name='errorMessage'),
    url(r'^messageDetail', views.messageDetail, name='messageDetail'),
    url(r'^exApproved', views.exApproved, name='exApproved'),
    url(r'^exUnapprove$', views.exUnapprove, name='exUnapprove'),
    url(r'^exNoTopic', views.exNoTopic, name='exNoTopic'),
    url(r'^detail_exUnapprove', views.detail_exUnapprove, name='detail_exUnapprove'),
    url(r'^detail_exApproved', views.detail_exApproved, name='detail_exApproved'),
    url(r'^add_tag', views.add_tag, name='add_tag'),
    url(r'^upprove_exercise_status', views.upprove_exercise_status, name='upprove_exercise_status'),
]
