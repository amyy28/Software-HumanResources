from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.



class Company(models.Model):
    class Meta:
        verbose_name_plural = 'companies'
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    CHOICES = (
        ('Fixed', (
            ('Fixed-Inclusive', 'Fixed-Inclusive'),
            ('Fixed-Exclusive', 'Fixed-Exclusive'),
        )),
        ('Percentage', (
            ('Percent-Inclusive', 'Percent-Inclusive'),
            ('Percent-Exclusive', 'Percent-Exclusive'),
        )),
    )
    CTC_TYPE = (
        ('Fixed', 'Fixed'),
        ('Gross', 'Gross'),
    )
    company_id = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    company_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    choice = models.CharField(max_length=20, choices=CHOICES, default='Fixed')
    CTC_type = models.CharField(max_length=20, choices=CTC_TYPE, blank=True, help_text="Only required if 'Percentage' attributes are selected.")
    value = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)
    #jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})
