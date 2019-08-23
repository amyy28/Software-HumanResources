from django.db import models
from django.urls import reverse
from Company.models import Company
from django.utils import timezone

# Create your models here.

class Jobb(models.Model):
    class Meta:
        verbose_name_plural = 'jobs'

    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('On-hold', 'On-hold'),
    )
    JOB_TYPES = (
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
    )
    job_id = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    JD_link = models.URLField(max_length=100)
    budget = models.CharField(max_length=100)
    submission_deadline = models.DateField()
    job_status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Open')
    job_type = models.CharField(max_length=100, choices=JOB_TYPES, default='Full-time')
    date_posted = models.DateTimeField(default=timezone.now)
    required_experience = models.CharField(max_length=100)
    #jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    def __str__(self):
        return self.position

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})
