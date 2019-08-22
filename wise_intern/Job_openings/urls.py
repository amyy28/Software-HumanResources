from django.urls import path
from . import views
from .views import (
    JobCreateView,
    JobUpdateView,
    JobDeleteView,
    JobDetailView,
    )


urlpatterns = [
    path('', views.jobs, name='jobs-list'),
    path('<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path('new/', JobCreateView.as_view(), name='job-create'),
]