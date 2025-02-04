from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('yfcase.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('accounts/', include('allauth.urls')),
    path('accounts/password/reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password/reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
