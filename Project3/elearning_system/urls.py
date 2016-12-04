from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('elearning_system.user.urls')),
]
