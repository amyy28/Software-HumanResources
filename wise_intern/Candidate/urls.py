from django.urls import path
from . import views
from .views import (
    CandidateCreateView,
    CandidateUpdateView,
    CandidateDeleteView,
    CandidateDetailView,
    contact_upload
    )

urlpatterns = [
    path('', views.candidate, name='candidate-list'),
    path('<int:pk>/', CandidateDetailView.as_view(), name='candidate-detail'),
    path('<int:pk>/update/', CandidateUpdateView.as_view(), name='candidate-update'),
    path('<int:pk>/delete/', CandidateDeleteView.as_view(), name='candidate-delete'),
    path('new/', CandidateCreateView.as_view(), name='candidate-create'),
    path('upload-csv/', contact_upload, name='contact_upload'),

]





