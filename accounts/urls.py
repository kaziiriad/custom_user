from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('regsiter/', views.register, name='register'),
    path('profile/<pk>', views.login, name='login'),
    path('success/', views.success_page, name='success'),
    

]
