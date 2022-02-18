from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import TypeSerializer, ContentSerializer
from .models import Type, Content


class ContentViewset(viewsets.ModelViewSet):
    queryset = Content.objects.all().order_by('id')
    serializer_class = ContentSerializer


class TypeViewset(viewsets.ModelViewSet):
    queryset = Type.objects.all().order_by('id')
    serializer_class = TypeSerializer
