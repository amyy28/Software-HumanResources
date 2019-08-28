from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.



class Vendor(models.Model):
    class Meta:
        verbose_name_plural = 'vendors'

    vendor_id = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    commission_rate = models.CharField(max_length=100)

    def __str__(self):
        return self.vendor_name

    def get_absolute_url(self):
        return reverse('vendor-detail', kwargs={'pk': self.pk})
