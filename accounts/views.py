from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView
from guest_user.views import ConvertFormView
from guest_user.mixins import AllowGuestUserMixin

# Create your views here.


# def success_page(request):

#     return render(request, 'accounts/success.html')

class HomeView(TemplateView):
    template_name = "accounts/home.html"

# def index(request):

#     return render(request, 'accounts/home.html')


# def register(request):

#     if request.method == 'POST':

#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')

#         if password == confirm_password:

#             if User.objects.filter(username=username).exists():

#                 messages.info(request, "Username already taken!")
#                 return redirect('register')

#             elif User.objects.filter(email=email).exists():

#                 messages.info(request, "Email already taken!")
#                 return redirect('register')

#             else:
                
#                 user = User.objects.create(
#                     username=username,
#                     password=password,
#                     email=email,
#                     first_name=first_name,
#                     last_name=last_name
#                 )
#                 user.save()
#                 messages.success(request, 'Registration Successful!')
#                 return redirect('login')

#         else:
#             messages.info(request, "Passwords are not matching!")
#             return redirect('register')


#     return render(request, 'accounts/register.html')

class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = NewUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    success_message = "Registration successful."
    



class MyConvertFormView(ConvertFormView):

    # form_class = NewUserForm
    template_name = "accounts/register.html"

convert_form = MyConvertFormView.as_view()

# def login_user(request):

#     if request.method == 'POST':

#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Invalid Username or Password')
#             return redirect('login')

#     return render(request, 'accounts/login.html')


# def view_user_profile(request):

#     user = User.objects.get(request.user)
#     context = {'user': user}

#     return render(request, 'accounts/profile.html', context)


# def delete_user(request, userid):
#     pass


# def logout_user(request):

#     logout(request)

#     return redirect('home')
