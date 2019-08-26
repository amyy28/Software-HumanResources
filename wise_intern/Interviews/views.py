from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Interview
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from Tracker.models import Tracker
from .forms import InterviewForm

# Create your views here.

@login_required
def interview(request):
    interviews = Interview.objects.all().order_by('-date_posted')
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        interviews = interviews.filter(interview_date__icontains=search_term)
    context = {
        'interviews': interviews, 'search_term': search_term, 'interview': 'active'
    }
    return render(request, 'Interviews/interview.html', context)


class InterviewCreateView(LoginRequiredMixin, CreateView):
    model = Interview
    form_class = InterviewForm

    def get_initial(self):
        tracker_id = self.request.GET.get('tracker_id')
        if tracker_id:
            try:
                tracker = Tracker.objects.get(id=tracker_id)
            except Tracker.DoesNotExist:
                return super().get_initial()
            return {'candidate': tracker.candidate_name,
                    'phone': tracker.phone,
                    'client': tracker.company_applied,
                    'position': tracker.position_applied,
                }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class InterviewDetailView(LoginRequiredMixin, DetailView):
    model = Interview

class InterviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Interview
    form_class = InterviewForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class InterviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Interview
    success_url = '/dashboard/interviews/'


def email(request):
    subject = 'Interview!!'
    message = ' Your interview has been scheduled. We wish you best luck! '
    template = get_template('Interviews/email-template.html')
    candidate_id = request.GET.get('interview_id')
    candidate = Interview.objects.get(id=candidate_id)
    context = {
        'candidate': candidate,
    }
    html_content = template.render(context)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['bhatnagar.aman1998@gmail.com',]
    msg = EmailMultiAlternatives( subject, message, email_from, recipient_list )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render(request, 'Interviews/email.html')


