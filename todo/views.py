from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:task-list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority', 'completed']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('todo:task-list')

# Toggle complete (POST)
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator

@require_POST
def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    next_url = request.POST.get('next', reverse_lazy('todo:task-list'))
    return redirect(next_url)
