from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='website-home'),
    path('profile/', views.profile, name='profile-list'),
]