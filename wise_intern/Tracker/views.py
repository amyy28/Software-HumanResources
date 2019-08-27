from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tracker
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from Job_openings.models import Jobb
from Candidate.models import Candidate
from django.db.models import Q

# Create your views here.

@login_required
def tracker(request):
    if request.user.is_superuser:
        tracker = Tracker.objects.all().order_by('-date_posted')
    else:
        tracker = Tracker.objects.filter(user=request.user).order_by('-date_posted')
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        tracker = tracker.filter(
            Q(company_applied__company_name__icontains=search_term) |
            Q(candidate_name__candidate_name__icontains=search_term) |
            Q(position_applied__position__icontains=search_term) |
            Q(phone__icontains=search_term)
        )
    context = {
        'tracker': tracker, 'search_term': search_term, 'tracker_page': 'active',
    }
    return render(request, 'Tracker/tracker.html', context)




class TrackerCreateView(LoginRequiredMixin, CreateView):
    model = Tracker
    fields = ['current_CTC', 'expected_CTC', 'notice_period', 'email','user','phone', 'company_applied', 'position_applied', 'candidate_status', 'relevant_experience', 'total_experience', 'candidate_name']

    def get_initial(self):
        candidate_id = self.request.GET.get('candidate_id')
        if candidate_id:
            try:
                candidate = Candidate.objects.get(id=candidate_id)
            except Candidate.DoesNotExist:
                return super().get_initial()
            return {'candidate_name': candidate,
                    'phone': candidate.phone,
                    'email': candidate.email,
                    'user':self.request.user,
                }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TrackerDetailView(LoginRequiredMixin, DetailView):
    model = Tracker

class TrackerUpdateView(LoginRequiredMixin, UpdateView):
    model = Tracker
    fields = ['current_CTC', 'expected_CTC', 'notice_period', 'company_applied', 'phone','user', 'email', 'position_applied', 'candidate_status', 'relevant_experience', 'total_experience', 'candidate_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TrackerDeleteView(LoginRequiredMixin, DeleteView):
    model = Tracker
    success_url = '/dashboard/tracker/'
