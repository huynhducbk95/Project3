from django.conf.urls import url, include

urlpatterns = [
    url(r'^user/', include('elearning_system.user.urls')),
    url(r'^exercise/', include('elearning_system.exercise.urls'),name='exercise'),
    # url(r'^query_expert', views.query_expert, name='query_expert')

]
