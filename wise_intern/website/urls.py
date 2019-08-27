from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('', views.home, name='website-home'),
    path('profile/', views.profile, name='profile-list'),
    path('profile/password/change/', PasswordChangeView.as_view(template_name= 'website/password_change_form.html'),
        name='password_change'),
    path('profile/password/change/done/', PasswordChangeDoneView.as_view(template_name= 'website/password_change_done.html'),
        name='password_change_done'),
]