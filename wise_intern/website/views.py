from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Candidate.models import Candidate
from Company.models import Company
from Job_openings.models import Jobb
from Tracker.models import Tracker
from django.db.models import Count

# Create your views here.

@login_required
def home(request):
    candidates = Candidate.objects.all().count()
    candidates_active = Tracker.objects.all().count()
    companies_active = Company.objects.filter(company_status='Active').count()
    job_openings = Jobb.objects.filter(job_status='Open').count()
    interview_scheduled = Tracker.objects.filter(candidate_status='Interview Scheduled').count()
    interviewed = Tracker.objects.filter(candidate_status='Interviewed').count()
    selected = Tracker.objects.filter(candidate_status='Selected').count()
    onhold = Tracker.objects.filter(candidate_status='On-hold').count()
    rejected = Tracker.objects.filter(candidate_status='Rejected').count()
    context = {
        "dashboard": "active", 'candidates':candidates, 'rejected':rejected, 'onhold':onhold, 'selected':selected, 'interviewed':interviewed, 'interview_scheduled':interview_scheduled, 'candidates_active':candidates_active, 'companies_active':companies_active, 'job_openings':job_openings,
               }
    return render(request, 'website/dashboard.html', context)


@login_required
def profile(request):
    context = {"profile": "active"}
    return render(request, 'website/profile.html', context)







