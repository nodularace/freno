
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^member/(?P<pk>[0-9]+)/$',
        views.TeamMemberDetail.as_view(), name="member-details"),
    url(r'^list-or-create-member/$',
        views.TeamMemberListOrCreate.as_view(), name="listcreate-member"),
]
