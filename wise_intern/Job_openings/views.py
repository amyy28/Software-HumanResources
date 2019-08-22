from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Jobb
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .forms import JobForm
from django.db.models import Q


# Create your views here.

@login_required
def jobs(request):
    jobs = Jobb.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        jobs = jobs.filter(
            Q(position__icontains=search_term) |
            Q(company__company_name__icontains=search_term) |
            Q(job_id__icontains=search_term)
        )
    context = {
        'jobs': jobs, 'search_term': search_term, 'job': 'active'
    }
    return render(request, 'Job_openings/jobb.html',context)


class JobCreateView(CreateView):
    model = Jobb
    form_class = JobForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class JobDetailView(LoginRequiredMixin, DetailView):
    model = Jobb

class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Jobb
    form_class = JobForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Jobb
    success_url = '/dashboard/jobs/'