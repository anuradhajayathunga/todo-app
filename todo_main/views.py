from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    comp_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    #print(comp_tasks)
    context = {
    'tasks': tasks,
    'comp_tasks': comp_tasks
    }
   # print(tasks)
    return render(request, 'home.html',context)
