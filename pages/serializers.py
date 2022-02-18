from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Type
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    content_type = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.Content
        fields = '__all__'
