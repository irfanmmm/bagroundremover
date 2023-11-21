from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from main.models import Removebaground


class RemovebagroundSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Removebaground
