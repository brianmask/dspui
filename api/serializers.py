"""
 api.serializers houses serializers for the api application
"""
from rest_framework import serializers

from api.models import (
    Story, StoryBoard
)

class DSPStorySerializer(serializers.ModelSerializer):
    """
    DSPStorySerializer - Serializer for Story Generation (Nav Items)
    Arguments:
        serializers {queryset} -- the default queryset to use
    """
    class Meta:
        model = Story
        fields = ('id', 'name', 'position', 'icon')

class DSPStoryPartsSerializer(serializers.ModelSerializer):
    """
    DSPStoryPartsSerializer - Serializer for Story parts (Tab Generation)

    Arguments:
        serializers {queryset} -- the default queryset to use
    """
    class Meta:
        model = StoryBoard
        fields = ('id', 'name', 'position', 'text')

class DSPStoryDetailSerializer(serializers.ModelSerializer):
    """
    DSPStoryDetailSerializer - Serializer for Story Detail

    Arguments:
        serializers {queryset} -- the default queryset to use
    """
    story = DSPStoryPartsSerializer(many=True)

    class Meta:
        model = Story
        fields = ('id', 'name', 'story')
