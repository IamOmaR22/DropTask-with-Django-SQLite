from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def index(request):

    return render(request, 'index.html')


def todolist(request):

    if request.method == 'POST':   ## If i want add anything in db
        form = TaskForm(request.POST or None) ## If i want add anything in db
        if form.is_valid():  ## If i want add anything in db
            form.save()

        messages.success(request, ("Task Added Successfully"))

        return redirect('todolist')

    else:
        all_tasks = TaskList.objects.all()   # it will fetch all the data inside all_task object(if i want to access anything)
        paginator = Paginator(all_tasks, 7)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})  ## all obj


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()

    return redirect('todolist')


def edit_task(request, task_id):

    if request.method == 'POST':   ## If i want add anything in db

        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task) ##instance=task means which task your are editing
        if form.is_valid():
            form.save()

        messages.success(request, ("Task Edited Successfully"))
        return redirect('todolist')

    else:
        task_obj = TaskList.objects.get(pk=task_id)     # it will fetch single data of that particular id

        return render(request, 'edit.html', {'task_obj': task_obj}) ## one obj (particular obj)


def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True ## When user mark it as completed
    task.save()

    return redirect('todolist')


def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False ## When user mark it as pending
    task.save()

    return redirect('todolist')


def contact(reqest):

    context = {
        'contact_text':"Welcome To Contact Page"
    }
    return render(reqest, 'contact.html', context)

def about(reqest):

    context = {
        'about_text':"Welcome To About Page"
    }
    return render(reqest, 'about.html', context)

