from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404

from api.models import (
    NavigationMenu,
)

from api.serializers import (
    DSPNavigationSerializer, DSPTabSerializer
)

class DSPNavigationBuilder(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def list(self, request):
        queryset = NavigationMenu.objects.filter(is_story=True)
        serializer = DSPNavigationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = NavigationMenu.objects.filter(is_story=True)
        story = get_object_or_404(queryset, pk=pk)
        serializer = DSPTabSerializer(story)
        return Response(serializer.data)
        