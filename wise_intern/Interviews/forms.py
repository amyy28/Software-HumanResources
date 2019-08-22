from django import forms
from django.forms import ModelForm

from .models import Interview


class DateInput(forms.DateInput):
    input_type = 'date'


class InterviewForm(ModelForm):

    class Meta:
        model = Interview
        fields = ['interview_date', 'interview_time', 'phone', 'candidate', 'mode', 'client','position', 'address', 'map_link', 'contact_person']
        widgets = {
            'interview_date': DateInput(),
        }