from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

from .models import Task
from .forms import UpdateTaskFormCustom

# Create your views here.
class HomeView(LoginRequiredMixin, ListView):
  model = Task
  paginate_by = 10
  
  def get_queryset(self):
    return Task.objects.filter(user_id=self.request.user)

class CreateTaskView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  model = Task
  fields = ['text']
  success_message = 'Task was created successfully'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class UpdateTaskView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = Task
  form_class = UpdateTaskFormCustom
  template_name_suffix = '_update_form'
  success_message = 'Task was updated successfully'

  def get_queryset(self):
    return Task.objects.filter(user_id=self.request.user)
