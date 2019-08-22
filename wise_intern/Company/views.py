from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Company
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Count
from django.db.models import Q

# Create your views here.

@login_required
@user_passes_test(lambda user: user.is_superuser)
def company(request):
    companies = Company.objects.annotate(njobs=Count('jobb', distinct=True)).annotate(ncandidates=Count('tracker', distinct=True))
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
    fields = ['company_id', 'company_name', 'city', 'state', 'contact_person', 'contact_phone', 'contact_email', 'company_status', 'CTC_type', 'value', 'choice']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company

class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['company_id', 'company_name', 'city', 'state', 'contact_person', 'contact_phone', 'contact_email', 'company_status', 'CTC_type', 'value', 'choice']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = '/dashboard/company/'
