"""
 models for the api application
"""
from django.db import models

# Create your models here.

class Story(models.Model):
    """
    Story - model to house stories which will be the navigation
            links for the un-authenticated user base
    """
    name = models.CharField(max_length=255)
    position = models.FloatField()
    icon = models.CharField(max_length=65)
    is_story = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'Stories'

class StoryBoard(models.Model):
    """
    StoryBoard - model to house the pieces making up the entire
                 story for navigation.
    """
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='story')
    position = models.FloatField()
    name = models.CharField(max_length=65)
    text = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.story.name, self.name)

    class Meta:
        ordering = ['position']
        