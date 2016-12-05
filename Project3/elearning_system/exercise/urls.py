from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^test_code$', views.test_code, name='test_code'),
    url(r'^solve_exercise', views.slove_exercise, name='solve_exercise'),
]
