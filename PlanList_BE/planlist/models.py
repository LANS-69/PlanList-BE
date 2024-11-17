from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)


class WishList(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    storeUrl = models.URLField()
    image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Location(models.TextChoices):
        LIVINGROOM = 'livingroom', 'Living Room'
        BATHROOM = 'bathroom', 'Bathroom'
        BEDROOM = 'bedroom', 'Bedroom'
        PLAYROOM = 'playroom', 'Playroom'
        KITCHEN = 'kitchen', 'Kitchen'
        BACKYARD = 'backyard', 'Backyard'
        OFFICE = 'office', 'Office'
        BALCONY = 'balcony', 'Balcony'
        OTHER = 'other', 'Other'
    
    location = models.CharField(max_length=10, choices=Location.choices)