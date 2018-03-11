from django.conf.urls import (
    url,
    include
)


urlpatterns = [
    url(r'^api/team/', include('teams.urls')),
]
