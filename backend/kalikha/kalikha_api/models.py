from django.db import models
from django.contrib.auth.models import User


class UpcyclerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    materials_needed = models.TextField(blank=True)
    location = models.CharField(max_length=50)


class ProviderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    typical_resources = models.CharField(max_length=255, blank=True)
    availability_frequency = models.CharField(max_length=255)
    location = models.CharField(max_length=50)


class ResourceListing(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    