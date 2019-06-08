"""
 api.serializers houses serializers for the api application
"""
from rest_framework import serializers

from api.models import (
    NavigationMenu, NavigationTab
)

class DSPNavigationSerializer(serializers.ModelSerializer):
    """
    DSPNavigationSerializer - Serializer for Story Generation (Nav Items)
    Arguments:
        serializers {queryset} -- the default queryset to use
    """
    class Meta:
        model = NavigationMenu
        fields = ('id', 'name', 'position', 'icon')

class DSPTabPartsSerializer(serializers.ModelSerializer):
    """
    DSPStoryPartsSerializer - Serializer for Story parts (Tab Generation)

    Arguments:
        serializers {queryset} -- the default queryset to use
    """
    class Meta:
        model = NavigationTab
        fields = ('id', 'name', 'position', 'text')

class DSPTabSerializer(serializers.ModelSerializer):
    """
    DSPStoryDetailSerializer - Serializer for Story Detail

    Arguments:
        serializers {queryset} -- the default queryset to use
    """
    menu = DSPTabPartsSerializer(many=True)

    class Meta:
        model = NavigationMenu
        fields = ('id', 'name', 'menu')
