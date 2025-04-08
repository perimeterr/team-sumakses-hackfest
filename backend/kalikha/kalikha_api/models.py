from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('provider', 'Resource Provider'),
        ('upcycler', 'Upcycler'),
    ]
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='provider',
    )

    def __str__(self):
        return self.username

class ResourceListing(models.Model):
    MATERIAL_CATEGORY_CHOICES = [
        ('textiles', 'Textiles'),
        ('plastics', 'Plastics'),
        ('food_waste', 'Food Waste'),
        ('wood', 'Wood'),
        ('paper_cardboard', 'Paper/Cardboard'),
        ('other', 'Other'),
    ]
    CONDITION_CHOICES = [
        ('new_surplus', 'New Surplus'),
        ('used_good', 'Used - Good Condition'),
        ('slightly_damaged', 'Slightly Damaged - Repairable'),
    ]
    AVAILABILITY_CHOICES = [
        ('free', 'Free for Pickup'),
        ('negotiable', 'Negotiable'),
        ('small_fee', 'Small Fee for Handling'),
    ] # to be edited

    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resource_listings')
    material_category = models.CharField(
        max_length=20,
        choices=MATERIAL_CATEGORY_CHOICES,
        verbose_name="Material Category"
    )
    description = models.TextField(verbose_name="Detailed Description of Materials")
    quantity = models.FloatField(verbose_name="Quantity/Volume")
    unit = models.CharField(max_length=20, verbose_name="Unit (e.g., kg, pieces, liters)")
    condition = models.CharField(
        max_length=30,
        choices=CONDITION_CHOICES,
        verbose_name="Condition"
    )
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        verbose_name="Availability"
    )
    location_barangay = models.CharField(max_length=100, verbose_name="Barangay")
    location_latitude = models.FloatField(blank=True, null=True, verbose_name="Latitude")
    location_longitude = models.FloatField(blank=True, null=True, verbose_name="Longitude")
    image = models.ImageField(upload_to='resource_images/', blank=True, null=True, verbose_name="Image")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.material_category} - {self.quantity} {self.unit} (by {self.provider.username})"

class UpcyclerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='upcycler_profile')
    name_or_organization = models.CharField(max_length=255, verbose_name="Name / Organization Name")
    areas_of_interest = models.TextField(blank=True, verbose_name="Areas of Upcycling Interest (e.g., Textile Upcycling, Plastic Art)")
    materials_needed = models.TextField(blank=True, verbose_name="Materials Needed (searchable keywords)")
    description = models.TextField(blank=True, verbose_name="Brief Description of Upcycling Activities/Skills (optional)")
    contact_information = models.TextField(verbose_name="Contact Information (visible to connected providers)")

    def __str__(self):
        return self.name_or_organization

class ProviderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='provider_profile')
    # Add other profile fields specific to providers if needed.  Include all the fields from the resource listing, and any others.
    company_name = models.CharField(max_length=255, blank=True, verbose_name="Company Name")
    address = models.TextField(blank=True, verbose_name="Company Address")
    contact_person = models.CharField(max_length=255, blank=True, verbose_name="Contact Person")
    material_category = models.CharField(
        max_length=20,
        choices=ResourceListing.MATERIAL_CATEGORY_CHOICES,
        verbose_name="Material Category"
    )
    description = models.TextField(verbose_name="Detailed Description of Materials")
    quantity = models.FloatField(verbose_name="Quantity/Volume")
    unit = models.CharField(max_length=20, verbose_name="Unit (e.g., kg, pieces, liters)")
    condition = models.CharField(
        max_length=30,
        choices=ResourceListing.CONDITION_CHOICES,
        verbose_name="Condition"
    )
    availability = models.CharField(
        max_length=20,
        choices=ResourceListing.AVAILABILITY_CHOICES,
        verbose_name="Availability"
    )
    location_barangay = models.CharField(max_length=100, verbose_name="Barangay")
    location_latitude = models.FloatField(blank=True, null=True, verbose_name="Latitude")
    location_longitude = models.FloatField(blank=True, null=True, verbose_name="Longitude")
    image = models.ImageField(upload_to='resource_images/', blank=True, null=True, verbose_name="Image")

    def __str__(self):
        return self.user.username


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    listing = models.ForeignKey(ResourceListing, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['sent_at']

    def __str__(self):
        return f"From {self.sender.username} to {self.recipient.username} on {self.listing}" if self.listing else f"From {self.sender.username} to {self.recipient.username}"