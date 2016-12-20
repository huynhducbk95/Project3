from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list_ex$', views.list_ex_of_topic, name='list_ex'),
    url(r'^search$', views.search, name='search'),
    url(r'^typeahead_search$', views.typeahead_search, name='typeahead_search'),
    url(r'^get_exercise_pagination', views.get_exercise_pagination, name='get_exercise_pagination'),
    url(r'^login', views.login, name='login'),
    url(r'^registry', views.registry, name='registry'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^user_infor', views.user_infor, name='user_infor'),
    url(r'^ranking', views.ranking, name='ranking'),
]
