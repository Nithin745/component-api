from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import TypeSerializer, ContentSerializer
from .models import Type, Content


class ContentViewset(viewsets.ModelViewSet):
    queryset = Content.objects.all().order_by('id')
    serializer_class = ContentSerializer

    def get_queryset(self):
        params = self.request.query_params.get('type', None)
        if params:
            content = Content.objects.select_related('type')
            if params == "header":
                content = content.filter(type__name=params)
            if params == "card":
                content = content.filter(type__name=params)
            print(content.values())
        return content


class TypeViewset(viewsets.ModelViewSet):
    queryset = Type.objects.all().order_by('id')
    serializer_class = TypeSerializer
