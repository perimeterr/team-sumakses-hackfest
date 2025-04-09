from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('provider', 'Resource Provider'),
        ('upcycler', 'Upcycler'),
    ]
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='provider',
    )
    name = models.CharField(max_length=255, verbose_name="Name") # Added Name
    description = models.TextField(blank=True, verbose_name="Description") # Added Description
    location = models.CharField(max_length=255, verbose_name="Location") # Added Location

    def __str__(self):
        return self.username

class MaterialCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('kalikha_api:material_detail', args=[self.pk])

class ResourceListing(models.Model):
    provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('kalikha_api:resource_listing_detail', args=[self.pk])

class ResourceMaterial(models.Model):
    """
    Represents a specific resource material within a Resource Listing.
    """
    resource_listing = models.ForeignKey(ResourceListing, on_delete=models.CASCADE)
    material_category = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE)
    quantity_unit = models.CharField(max_length=50, help_text="e.g.: 4 kg, 5 pcs")
    description = models.TextField(blank=True, null=True)
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Used (Like New)', 'Used (Like New)'),
        ('Used (Good)', 'Used (Good)'),
        ('Used (Fair)', 'Used (Fair)'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    TYPE_CHOICES = [
        ('Textiles', 'Textiles'),
        ('Plastics', 'Plastics'),
        ('Wood', 'Wood'),
        ('Paper/Cardboard', 'Paper/Cardboard'),
        ('Glass Bottles', 'Glass Bottles'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    class Meta:
        verbose_name_plural = "Resource Materials"