from django.db import models
from django.conf import settings

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=264, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True) 

    def __str__(self):
        return f"{self.user.username}'s Billing Address" 

    def is_fully_filled(self):  # Corrected method name
        required_fields = ['address', 'zipcode', 'city', 'country', 'phone_number']
        for field_name in required_fields:
            value = getattr(self, field_name)
            if value is None or value.strip() == '':
                return False
        return True

    class Meta:
        verbose_name_plural = "Billing Addresses"
