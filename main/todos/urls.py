from django.urls import path, include
from .views import HomeView, CreateTaskView, UpdateTaskView

urlpatterns = [
    path('', HomeView.as_view(), name='todos-index'),
    path('create', CreateTaskView.as_view(), name='todos-create'),
    path('<int:pk>/update', UpdateTaskView.as_view(), name='todos-update'),
]
