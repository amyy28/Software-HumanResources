from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.



class Interview(models.Model):
    interview_date = models.CharField(max_length=10)
    date_posted = models.DateTimeField(default=timezone.now)
    interview_time = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    map_link = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    candidate = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.candidate

    def get_absolute_url(self):
        return reverse('interview-detail', kwargs={'pk': self.pk})

