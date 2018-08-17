from django import forms
from .models import Task

class UpdateTaskFormCustom(forms.ModelForm):
  text         = forms.CharField(disabled=True)
  is_completed = forms.BooleanField(required=False, widget=forms.CheckboxInput(
    attrs={'class': 'form-check-input'}
  ))

  class Meta:
    model = Task
    fields = ['text', 'is_completed']