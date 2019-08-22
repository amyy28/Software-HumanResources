from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from Candidate.models import Candidate
from Company.models import Company
from django.utils import timezone

# Create your models here.



class Tracker(models.Model):
    class Meta:
        verbose_name_plural = 'tracker'

    STATUS_CHOICES = (
        ('Submitted', 'Submitted'),
        ('Interview Scheduled', 'Interview Scheduled'),
        ('Shortlisted', 'Shortlisted'),
        ('Interviewed', 'Interviewed'),
        ('Selected', 'Selected'),
        ('On-hold', 'On-hold'),
        ('Rejected', 'Rejected'),
    )
    company_applied = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate_name = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidates')
    position_applied = models.CharField(max_length=100)
    current_CTC = models.CharField(max_length=100)
    expected_CTC = models.CharField(max_length=100)
    notice_period = models.CharField(max_length=100)
    candidate_status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Submitted')
    relevant_experience = models.CharField(max_length=100)
    total_experience = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.position_applied

    def get_absolute_url(self):
        return reverse('tracker-detail', kwargs={'pk': self.pk})