from django.contrib import admin

# Register your models here.

from api.models import (
    Story, StoryBoard
)

admin.site.register(Story)
admin.site.register(StoryBoard)