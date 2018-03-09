from __future__ import absolute_import

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import TeamMemberSerializer

from .models import Member


class TeamMemberListOrCreate(generics.ListCreateAPIView):
    """
    Team Member List API
    """
    permission_classes = (AllowAny, )
    queryset = Member.objects.all()
    serializer_class = TeamMemberSerializer


class TeamMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Member.objects.all()
    serializer_class = TeamMemberSerializer


