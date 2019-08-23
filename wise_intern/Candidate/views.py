from django.shortcuts import render
import csv, io
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Candidate
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

# Create your views here.

@login_required
def candidate(request):
    candidates = Candidate.objects.all().order_by('-date_posted')
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        candidates = candidates.filter(
            Q(candidate_name__icontains=search_term) |
            Q(phone__icontains=search_term)
        )
    context = {
        'candidates': candidates, 'search_term': search_term, 'candidate': 'active'
    }
    return render(request, 'Candidate/candidate.html', context)



class CandidateCreateView(LoginRequiredMixin, CreateView):
    model = Candidate
    fields = ['candidate_name', 'experience_years' , 'experience_months', 'phone', 'comments', 'email', 'PAN_number', 'current_company', 'current_location', 'preferred_location', 'skills', 'current_designation']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CandidateDetailView(LoginRequiredMixin, DetailView):
    model = Candidate

class CandidateUpdateView(LoginRequiredMixin, UpdateView):
    model = Candidate
    fields = ['candidate_name', 'experience_years', 'phone', 'comments', 'email', 'PAN_number', 'current_company', 'current_location', 'preferred_location', 'skills', 'current_designation', 'experience_months']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CandidateDeleteView(LoginRequiredMixin, DeleteView):
    model = Candidate
    success_url = '/dashboard/candidate/'


def contact_upload(request):
    template = "Candidate/contact_upload.html"

    prompt = {
        'order': 'Order of the csv file should be candidate_name, experience, new_experience, phone, email, PAN_number, current_company, current_location, preferred_location, current_designation, skills'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = Candidate.objects.update_or_create(
            candidate_name = column[0],
            experience_years = column[1],
            experience_months = column[2],
            phone = column[3],
            email = column[4],
            PAN_number = column[5],
            current_company = column[6],
            current_location = column[7],
            preferred_location = column[8],
            current_designation = column[9],
            comments=column[10],
            skills = column[11],
        )
    context = {}
    return render(request, template, context)













