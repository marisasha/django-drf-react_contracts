from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django_app import models



class ContractSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contract
        fields = "__all__"


class AgentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agent
        fields = "__all__"
