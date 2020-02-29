from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.forms import TaskForm

# Create your views here.

def todolist(reqest):

    if reqest.method == 'POST':
        form = TaskForm(reqest.POST or None)
        if form.is_valid():
            form.save()
        return redirect('todolist')

    else:
        all_tasks = TaskList.objects.all() # it will fetch all the data inside all_task object

        return render(reqest, 'todolist.html', {'all_tasks': all_tasks})

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