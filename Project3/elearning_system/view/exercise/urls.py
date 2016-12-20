from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test_code$', views.test_code, name='test_code'),
    # url(r'^exercise_detail_without_login', views.exercise_detail_without_login, name='exercise_detail_without_login'),
    url(r'^exercise_detail', views.exercise_detail, name='exercise_detail'),
    url(r'^report_exercise_error', views.report_exercise_error, name='report_exercise_error'),
    url(r'^contribute_exercise', views.contribute_exercise, name='contribute_exercise'),
    url(r'^solve_exercise', views.solve_exercise, name='solve_exercise'),

]
