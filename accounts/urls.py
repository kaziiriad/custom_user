from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('convert/', views.convert_form, name='guest_user_convert'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/home.html"), name='logout'),
    path('regsiter/', views.RegistrationView.as_view(), name='register'),
    # path('profile/<pk>', views.view_user_profile, name='profile'),
    # path('success/', views.success_page, name='success_page'),


]
