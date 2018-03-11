from __future__ import absolute_import

from rest_framework import serializers

from .models import Member


class TeamMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'
