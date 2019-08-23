from django.urls import path
from . import views
from .views import (
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView,
    CompanyDetailView,
    company_upload,
    )


urlpatterns = [
    path('', views.company, name='company-list'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('<int:pk>/update/', CompanyUpdateView.as_view(), name='company-update'),
    path('<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),
    path('new/', CompanyCreateView.as_view(), name='company-create'),
    path('upload-csv/', company_upload, name='company_upload'),
]