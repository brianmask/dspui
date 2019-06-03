from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404

from api.models import (
    Story, #StoryBoard
)

from api.serializers import (
    DSPStorySerializer, DSPStoryDetailSerializer
)

class DSPStoryBoard(viewsets.ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def list(self, request):
        queryset = Story.objects.filter(is_story=True)
        serializer = DSPStorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Story.objects.filter(is_story=True)
        story = get_object_or_404(queryset, pk=pk)
        serializer = DSPStoryDetailSerializer(story)
        return Response(serializer.data)
        