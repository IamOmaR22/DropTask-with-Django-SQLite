from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import TaskList, Contact
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required  ## for adding page restrictions

# Create your views here.

def index(request):

    return render(request, 'index.html')


@login_required
def todolist(request):

    if request.method == 'POST':   ## If i want add anything in db
        form = TaskForm(request.POST or None) ## If i want add anything in db
        if form.is_valid():  ## If i want add anything in db
            instance = form.save(commit=False)  ## commit=False, to access manager
            instance.manager = request.user
            instance.save()

        messages.success(request, ("Task Added Successfully"))

        return redirect('todolist')

    else:
        # all_tasks = TaskList.objects.all()   # it will fetch all the data inside all_task object(if i want to access anything)
        all_tasks = TaskList.objects.filter(manager=request.user) ## Task of logged in user only
        paginator = Paginator(all_tasks, 7)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})  ## all obj


@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()

    else:
        messages.error(request, 'Access Restricted, You Are Not Allowed!')

    return redirect('todolist')


@login_required
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


@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done = True ## When user mark it as completed
        task.save()

    else:
        messages.error(request, 'Access Restricted, You Are Not Allowed!')

    return redirect('todolist')


@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False ## When user mark it as pending
    task.save()

    return redirect('todolist')



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly!")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been sent successfully!')
    return render(request, 'contact.html')



def about(reqest):

    context = {
        'about_text':"Welcome To About Page"
    }
    return render(reqest, 'about.html', context)
