from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^manageTopic', views.manageTopic, name='admin'),
]
