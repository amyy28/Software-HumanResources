from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime

# Create your models here.

class Candidate(models.Model):
    candidate_name = models.CharField(max_length=100)
    experience_years = models.CharField(max_length=100)
    experience_months = models.CharField(max_length=100, help_text="Max. upto 12. If more, consider incrementing years.")
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    PAN_number = models.CharField(max_length=100, null=True, blank=True)
    current_company = models.CharField(max_length=100)
    current_location = models.CharField(max_length=100)
    preferred_location = models.CharField(max_length=100)
    current_designation = models.CharField(max_length=100)
    comments = models.CharField(max_length=100, null=True, blank=True)
    skills = models.CharField(max_length=1000,help_text="Add the skill followed by comma or space")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.candidate_name

    def get_absolute_url(self):
        return reverse('candidate-detail', kwargs={'pk': self.pk})