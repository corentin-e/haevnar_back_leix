from django.db import models
from discordlogin.models import DiscordUser
from rest_framework import serializers

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    emplacement = models.CharField(max_length=100)
    date = models.DateTimeField()
    created_by = models.ForeignKey(DiscordUser, on_delete=models.CASCADE, blank=True)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'