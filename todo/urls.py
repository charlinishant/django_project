from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('task/add/', views.TaskCreateView.as_view(), name='task-add'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-edit'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/toggle/', views.toggle_complete, name='task-toggle'),
]
