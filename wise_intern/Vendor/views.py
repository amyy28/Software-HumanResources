from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vendor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Count
from django.db.models import Q
from Tracker.models import Tracker

# Create your views here.

@login_required
@user_passes_test(lambda user: user.is_superuser)
def vendor(request):
    vendors = Vendor.objects.annotate(ncandidates=Count('tracker', distinct=True))
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        vendors = vendors.filter(
            Q(vendor_name__icontains=search_term) |
            Q(contact_phone__icontains=search_term)
        )
    context = {
        'vendors': vendors, 'search_term': search_term, 'vendor': 'active',
    }
    return render(request, 'Vendor/vendor.html', context)



class VendorCreateView(LoginRequiredMixin, CreateView):
    model = Vendor
    fields = ['vendor_id', 'vendor_name', 'city', 'state', 'contact_person', 'contact_phone', 'contact_email', 'commission_rate']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class VendorDetailView(LoginRequiredMixin, DetailView):
    model = Vendor

class VendorUpdateView(LoginRequiredMixin, UpdateView):
    model = Vendor
    fields = ['vendor_id', 'vendor_name', 'city', 'state', 'contact_person', 'contact_phone', 'contact_email', 'commission_rate']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VendorDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendor
    success_url = '/dashboard/vendor/'
