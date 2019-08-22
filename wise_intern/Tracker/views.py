from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tracker
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from Job_openings.models import Jobb
from Candidate.models import Candidate

# Create your views here.

@login_required
def tracker(request):
    tracker = Tracker.objects.filter(user=request.user)
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        tracker = tracker.filter(company_applied__icontains=search_term)
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
