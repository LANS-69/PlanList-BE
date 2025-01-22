from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=255)
    trailerLink = models.URLField(blank=True, max_length=2000)
    image = models.URLField(blank=True, max_length=2000)
    
    class Genre(models.TextChoices):
        ACTION = 'ACTION', 'Action'
        COMEDY = 'COMEDY', 'Comedy'
        DRAMA = 'DRAMA', 'Drama'
        HORROR = 'HORROR', 'Horror'
        ROMANCE = 'ROMANCE', 'Romance'
        SCIFI = 'SCIFI', 'Science Fiction'  
        FANTASY = 'FANTASY', 'Fantasy'      
        DOCUMENTARY = 'DOCUMENTARY', 'Documentary'
        OTHER = 'other', 'Other'

    mainGenre = models.CharField(max_length=20, choices=Genre.choices, blank=True)
    subGenre = models.CharField(max_length=20, choices=Genre.choices, blank=True)



class WishList(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    storeUrl = models.URLField(blank=True, max_length=2000)
    image = models.URLField(blank=True, null=True)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)

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


class TvShow(models.Model):
    name = models.CharField(max_length=255)
    trailerLink = models.URLField(blank=True, max_length=2000)
    image = models.URLField(blank=True, max_length=2000)
    
    class Genre(models.TextChoices):
        ACTION = 'ACTION', 'Action'
        COMEDY = 'COMEDY', 'Comedy'
        DRAMA = 'DRAMA', 'Drama'
        HORROR = 'HORROR', 'Horror'
        ROMANCE = 'ROMANCE', 'Romance'
        SCIFI = 'SCIFI', 'Science Fiction'  
        FANTASY = 'FANTASY', 'Fantasy'      
        DOCUMENTARY = 'DOCUMENTARY', 'Documentary'
        OTHER = 'other', 'Other'

    mainGenre = models.CharField(max_length=20, choices=Genre.choices, blank=True)
    subGenre = models.CharField(max_length=20, choices=Genre.choices, blank=True)
