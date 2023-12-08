from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('regsiter/', views.register, name='register'),
    path('profile/<pk>', views.view_user_profile, name='profile'),
    path('success/', views.success_page, name='success_page'),
    

]
