from django.urls import path
from . import views
from .views import (
    TrackerCreateView,
    TrackerUpdateView,
    TrackerDeleteView,
    TrackerDetailView,
    )


urlpatterns = [
    path('', views.tracker, name='tracker-page'),
    path('<int:pk>/', TrackerDetailView.as_view(), name='tracker-detail'),
    path('<int:pk>/update/', TrackerUpdateView.as_view(), name='tracker-update'),
    path('<int:pk>/delete/', TrackerDeleteView.as_view(), name='tracker-delete'),
    path('new/', TrackerCreateView.as_view(), name='tracker-create'),
]