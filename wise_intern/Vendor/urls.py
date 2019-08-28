from django.urls import path
from . import views
from .views import (
    VendorCreateView,
    VendorUpdateView,
    VendorDeleteView,
    VendorDetailView,
    )


urlpatterns = [
    path('', views.vendor, name='vendor-list'),
    path('<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('<int:pk>/update/', VendorUpdateView.as_view(), name='vendor-update'),
    path('<int:pk>/delete/', VendorDeleteView.as_view(), name='vendor-delete'),
    path('new/', VendorCreateView.as_view(), name='vendor-create'),
]