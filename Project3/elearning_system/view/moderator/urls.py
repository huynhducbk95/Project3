from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^errorMessage', views.errorMessage, name='errorMessage'),
    url(r'^messageDetail', views.messageDetail, name='messageDetail'),
    url(r'^exApproved', views.exApproved, name='exApproved'),
    url(r'^exUnapprove$', views.exUnapprove, name='exUnapprove'),
    url(r'^exNoTopic', views.exNoTopic, name='exNoTopic'),
    url(r'^detail_exUnapprove', views.detail_exUnapprove, name='detail_exUnapprove'),
    url(r'^add_tag', views.add_tag, name='add_tag'),
    url(r'^upprove_exercise_status', views.upprove_exercise_status, name='upprove_exercise_status'),
    url(r'^cancel_exercise_status', views.cancel_exercise_status, name='cancel_exercise_status'),
    url(r'^delete_exercise_status', views.delete_exercise_status, name='delete_exercise_status'),
    url(r'^redirect_status_approved', views.redirect_status_approved, name='redirect_status_approved'),
]
