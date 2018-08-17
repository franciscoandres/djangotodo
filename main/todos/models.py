from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
  text         = models.CharField(max_length=100, null=False, help_text='Required')
  is_completed = models.BooleanField(default=False)
  created_at   = models.DateTimeField(auto_now_add=True)
  user         = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    ordering = ('-created_at',)

  def get_absolute_url(self):
    return reverse('todos-index')