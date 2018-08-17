from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm

# Create your views here.
class RegisterUser(CreateView):
  form_class = RegisterUserForm
  template_name = 'register.html'
  success_url = reverse_lazy('login')
