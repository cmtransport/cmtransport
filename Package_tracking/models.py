import uuid
from django.db import models

class Package(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('pre-transit', 'pre-transit'),
        ('in_transit', 'In Transit'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]

    MESSAGES_CHOICES = [
        ('billing_information_received', 'Billing Information Received'),
        ('origin_scan', 'Origin Scan'),
        ('departure_scan', 'Departure Scan'),
        ('arrival_scan', 'Arrival Scan'),
        ('out_for_dilivery', 'Out For Dilivery'),
        ('delivered', 'Delivered'),
    ]

    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    receiver_location = models.CharField(max_length=200)
    receiver_email = models.EmailField()
    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    message = models.CharField(max_length=50, choices=MESSAGES_CHOICES, default='processing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tracking_id} - {self.receiver_name}"
