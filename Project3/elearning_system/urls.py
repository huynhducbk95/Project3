from django.conf.urls import url, include

urlpatterns = [
    # url(r'^', include('elearning_system.admin.urls')),
    # url(r'^moderator/', include('elearning_system.moderator.urls')),
    # url(r'^user/', include('elearning_system.user.urls')),
    # url(r'^exercise/', include('elearning_system.exercise.urls'),name='exercise'),
    url(r'^admin/', include('elearning_system.views.admin.urls')),
    url(r'^moderator/', include('elearning_system.views.moderator.urls')),
    url(r'^', include('elearning_system.views.user.urls')),
    url(r'^exercise/', include('elearning_system.views.exercise.urls'), name='exercise'),
    # url(r'^query_expert', views.query_expert, name='query_expert')

]
