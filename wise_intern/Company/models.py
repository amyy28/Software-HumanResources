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
            ('Fixed-Inclusive of all Taxes', 'Fixed-Inclusive of all Taxes'),
            ('Fixed-Exclusive of all Taxes', 'Fixed-Exclusive of all Taxes'),
        )),
        ('Percentage', (
            ('Percent-Inclusive of all Taxes', 'Percent-Inclusive of all Taxes'),
            ('Percent-Exclusive of all Taxes', 'Percent-Exclusive of all Taxes'),
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
    commercials = models.CharField(max_length=100, choices=CHOICES, default='Fixed')
    CTC_type = models.CharField(max_length=100, choices=CTC_TYPE, blank=True, help_text="Only required if 'Percentage' attributes are selected.")
    value = models.CharField(max_length=100, help_text="Enter ₹ for Fixed, % for Percentage")
    date_posted = models.DateTimeField(default=timezone.now)
    #jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})
