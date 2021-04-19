from django.http.response import HttpResponse
from task import models
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views import View
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate, login
from task.models import  Project, Entry


class RegisterView(CreateView):
    model = User
    fields = ['username', 'email', 'password']
    template_name = "authentication/register.html"
    success_url = reverse_lazy('task')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)
        print(user)
        if user.password == password:
            login(request, user)
            return redirect('/')
    return render(request, 'authentication/login.html')


class ProjectView(View):
    def get(self, request, *args, **kwargs):
        projects = request.user.projects.all()
        return render(request, 'task/project.html', {'projects': projects})
    
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        Project.objects.create(name=name, user=request.user)
        projects = request.user.projects.all()
        return render(request, 'task/project.html', {'projects': projects})


class TaskView(TemplateView):
    def get(self, request, *args, **kwargs):
        entries = request.user.entries.all()
        projects = request.user.projects.all()
        return render(request, 'task/task.html', {'entries': entries, 'projects': projects})
    
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        project = request.POST['project']
        print(name, start_time,end_time, project)

        Entry.objects.create(name=name, start_time=start_time, end_time=end_time, project_id=project, user=request.user)
        entries = request.user.entries.all()
        projects = request.user.projects.all()
        
        return render(request, 'task/task.html', {'entries': entries, 'projects': projects})