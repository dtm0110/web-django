from django import urls
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
#    path('login/', views.user_login , name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    # path('password-change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    # path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    # path('', views.dashboard, name='dashboard'),
] 