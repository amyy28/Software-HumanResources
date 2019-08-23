from django import forms
from django.forms import ModelForm

from .models import Jobb


class DateInput(forms.DateInput):
    input_type = 'date'


class JobForm(ModelForm):

    class Meta:
        model = Jobb
        fields = ['job_id', 'position', 'company', 'location', 'JD_link', 'required_experience', 'job_status', 'budget', 'submission_deadline', 'job_type']
        widgets = {
            'submission_deadline': DateInput(),
        }