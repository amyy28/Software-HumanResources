from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    context = {"dashboard": "active"}
    return render(request, 'website/dashboard.html', context)


@login_required
def profile(request):
    context = {"profile": "active"}
    return render(request, 'website/profile.html', context)







