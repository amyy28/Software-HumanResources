from django.urls import path
from . import views
from .views import (
    InterviewCreateView,
    InterviewUpdateView,
    InterviewDeleteView,
    InterviewDetailView,
    )

urlpatterns = [
    path('', views.interview, name='interview-page'),
    path('email/', views.email, name='email-page'),
    path('<int:pk>/', InterviewDetailView.as_view(), name='interview-detail'),
    path('<int:pk>/update/', InterviewUpdateView.as_view(), name='interview-update'),
    path('<int:pk>/delete/', InterviewDeleteView.as_view(), name='interview-delete'),
    path('new/', InterviewCreateView.as_view(), name='interview-create'),
]


