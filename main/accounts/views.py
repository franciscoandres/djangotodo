from django.shortcuts import render
from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.views.generic import CreateView

# Create your views here.
class RegisterUser(CreateView):
  form_class = RegisterUserForm
  template_name = 'register.html'
  success_url = reverse_lazy('login')
