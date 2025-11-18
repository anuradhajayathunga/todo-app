from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.- business logic here
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')
    #return HttpResponse(pk)

def mark_as_undone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')
    #return HttpResponse(pk)

def edit_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk) #request types -> get_task
    if request.method == 'POST':
        get_update_task = request.POST['task']
        get_task.task = get_update_task
        get_task.save()
        return redirect('home')

    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'edit_task.html',context)
    

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')