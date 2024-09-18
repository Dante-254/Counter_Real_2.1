from django.db import models


class Listing(models.Model):
    LISTING_TYPE_CHOICES = [
        ('B', 'Buy'),
        ('R', 'Rent'),
    ]
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_type = models.CharField(max_length=1, choices=LISTING_TYPE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return f"{self.bedrooms} bed, {self.bathrooms} bath, ${self.price} ({self.get_listing_type_display()})"


# from django.db import models

# Create your models here.
# class Listing(models.Model):
#     TYPE_CHOICES = [
#         ('buy', 'Buy'),
#         ('rent', 'Rent'),
#     ]
    
#     bedrooms = models.IntegerField()
#     bathrooms = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     listing_type = models.CharField(max_length=4, choices=TYPE_CHOICES)
#     description = models.TextField()
    
#     def __str__(self):
#         return f"{self.bedrooms} bed, {self.bathrooms} bath, ${self.price} ({self.get_listing_type_display()})"

