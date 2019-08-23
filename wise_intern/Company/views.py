from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Company
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.decorators import permission_required

# Create your views here.

@login_required
@user_passes_test(lambda user: user.is_superuser)
def company(request):
    companies = Company.objects.annotate(njobs=Count('jobb', distinct=True)).annotate(ncandidates=Count('tracker', distinct=True)).order_by('-date_posted')
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        companies = companies.filter(
            Q(company_name__icontains=search_term) |
            Q(company_id__icontains=search_term)
        )
    context = {
        'companies': companies, 'search_term': search_term, 'company': 'active'
    }
    return render(request, 'Company/company.html', context)



class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['company_id', 'company_name', 'city', 'state', 'contact_person', 'contact_phone', 'contact_email', 'company_status', 'CTC_type', 'value', 'commercials']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company

class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['company_id', 'company_name', 'city', 'state', 'contact_person', 'contact_phone', 'contact_email', 'company_status', 'CTC_type', 'value', 'commercials']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = '/dashboard/company/'

@permission_required('admin.can_add_log_entry')
def company_upload(request):
    template = "Company/company_upload.html"

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
        _, created = Company.objects.update_or_create(
            company_id = column[0],
            company_name = column[1],
            city = column[2],
            state = column[3],
            contact_person = column[4],
            contact_phone = column[5],
            contact_email = column[6],
            company_status = column[7],
            commercials = column[8],
            CTC_type = column[9],
            value = column[10],
        )
    context = {}
    return render(request, template, context)
