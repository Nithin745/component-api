from rest_framework import serializers
from . import models


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Type
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Content
        fields = ('main_content', 'sub_content', 'image', 'type', 'file', 'url')
