from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Commodity(models.Model):
    ITEM_CATEGORIES = [
        ('electronics', 'Electronics'),
        ('furniture', 'Furniture'),
        ('vehicles', 'Vehicles'),
        # Add more categories as needed
    ]

    item_name = models.CharField(max_length=255)
    item_description = models.TextField()
    quote_price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    item_category = models.CharField(max_length=50, choices=ITEM_CATEGORIES)
    status = models.CharField(max_length=50, default='listed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Bid(models.Model):
    commodity = models.ForeignKey(Commodity, related_name='bids', on_delete=models.CASCADE)
    bid_price_month = models.DecimalField(max_digits=10, decimal_places=2)
    rental_duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
