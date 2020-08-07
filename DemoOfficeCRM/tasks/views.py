from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, HttpResponse
from .models import User, UserDetail, Task, TasksStatus
from .forms import UserForm, UserDetailForm, TaskForm, PopupForm, Popup
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.core.paginator import Paginator
from datetime import datetime, timedelta, time


# Create your views here.

def handle_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            messages.success(request, 'Welcome To Dashboard')
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, 'Credentials do not match')
            return render(request, 'login.html')
    else:
        if request.user.is_authenticated:
            return redirect('/dashboard')

        return render(request, 'login.html')


def handle_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return render(request, 'login.html')


@login_required
def task_base(request):
    dashboard = 'test'
    context = {
        'dashboard': 'True',
        'title': 'Dashboard',
        'popups': Popup.objects.all()
    }
    return render(request, 'dashboard.html', context=context)


@login_required
def list_users(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = UserDetailForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user_model = form1.save(commit=False)
            user_model.password = make_password(form1.cleaned_data['password'])
            user_model.save()
            detail_model = form2.save(commit=False)
            detail_model.user_id = user_model.id
            detail_model.save()
            messages.success(request, 'User Created Successfully')
        else:
            messages.error(request, "User could not be created")

        return redirect('/list-users')

    else:
        users = User.objects.all()
        userF = UserForm()
        details = UserDetailForm()
        context = {
            'users': users,
            'userF': userF,
            'details': details,
            'title': 'Users Management'
        }
        return render(request, 'users/list_users.html', context=context)


# def delete_user(request):
#     if request.method == 'GET':
#         id = request.GET.get('id')
#         user = User.objects.get(id=id)
#         user.delete()
#
#         return HttpResponse('True')

@login_required
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        messages.success(request, 'User Deleted Successfully')
    except:
        messages.success(request, 'User Could not be deleted')

    return redirect('users')


def update_user_details(request):
    pass


@login_required
def tasks_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Successfully Assigned')
            return redirect('/tasks')
        else:
            messages.error(request, 'Please Enter Valid Data')
            return redirect('/tasks')

    else:
        # tasks_list = Task.objects.all()
        # paginator = Paginator(tasks_list, 2)
        # page = request.GET.get('page')
        # tasks_list = paginator.get_page(page)
        # context = {
        #     'tasks': 'test',
        #     'title': 'Tasks Assigned',
        #     'task_form': TaskForm(),
        #     'tasks_list': tasks_list
        # }
        tasks_list = Task.objects.all()
        # number_of_item = 4
        # paginatorr = Paginator(tasks_list, number_of_item)
        # first_page = paginatorr.page(1).object_list
        # page_range = paginatorr.page_range

        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_list = Task.objects.filter(created_at__lte=tomorrow, created_at__gte=today)

        context = {
            'tasks': 'test',
            'title': 'Tasks Assigned',
            'task_form': TaskForm(),
            # 'paginatorr': paginatorr,
            # 'first_page': first_page,
            # 'page_range': page_range,
            'today_list': today_list,
            'tasks_list': tasks_list
        }
        return render(request, 'tasks/tasks.html', context=context)


#
# def pagination(request):
#     tasks_list = Task.objects.all()
#     number_of_item = 4
#     paginatorr = Paginator(tasks_list, number_of_item)
#     if request.method == 'POST':
#         page_n = request.POST.get('page_n', None)
#         results = list(
#             paginatorr.page(page_n).object_list.values('id', 'title', 'description',
#             'owner', 'assignee', 'description','start_date', 'end_date', 'reminder_date'))
#         return JsonResponse({"results": results})

@login_required
def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, 'Task Deleted Successfully')
    except:
        messages.success(request, 'Task Could not be deleted')

    return redirect('tasks')


@login_required
def your_task(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)

    today_list = Task.objects.filter(created_at__lte=tomorrow, created_at__gte=today).filter(
        assignee_id=request.user.id)
    tasks_list = Task.objects.filter(assignee_id=request.user)
    incomplete_list = Task.objects.filter(assignee_id=request.user).filter(tasksstatus__completed='False')

    context = {
        'yourtask': 'test',
        'title': 'Your Tasks',
        'today_list': today_list,
        'tasks_list': tasks_list,
        'incomplete_list': incomplete_list
    }
    return render(request, 'tasks/yourtask.html', context=context)


@login_required
def popup(request):
    if request.method == 'POST':
        form = PopupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'POPUP Created Successfully')
            return redirect('/popup')
        else:
            messages.success(request, 'Form Invalid')
            return redirect('/popup')
    context = {
        'popup': 'popup',
        'title': 'POPUPs',
        'popupF': PopupForm(),
        'popupsobj': Popup.objects.all()

    }
    return render(request, 'notices/popup.html', context=context)
