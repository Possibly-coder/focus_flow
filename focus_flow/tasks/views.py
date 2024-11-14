from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm

class IndexView(generic.ListView):
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Todo.objects.order_by('-created_at')

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority')

        if title and priority:
            Todo.objects.create(title=title, priority=priority)
        return redirect('tasks:index')  # Redirect to the task list page after adding

    return render(request, 'tasks/tasks.html')

def delete(request, tasks_id):
    todo = get_object_or_404(Todo, pk=tasks_id)
    todo.delete()
    return redirect('tasks:index')

def update(request, tasks_id):
    todo = get_object_or_404(Todo, pk=tasks_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if 'isCompleted' in request.POST:
            form.instance.isCompleted = True
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'tasks/update_task.html', {'form': form, 'task': todo})

def toggle_complete(request, tasks_id):
    todo = get_object_or_404(Todo, pk=tasks_id)
    todo.isCompleted = not todo.isCompleted
    todo.save()
    return JsonResponse({'status': 'success', 'isCompleted': todo.isCompleted})

def contact(request):
    return render(request, 'tasks/contact.html')

def about(request):
    return render(request, 'tasks/about_page.html')