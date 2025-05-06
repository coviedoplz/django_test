from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render
from .forms import CreateNewTask

# Create your views here.
def index(request):
    title = 'Django course!!'
    return render(request, 'index.html', {'title' : title})

def about(request):
    username = 'el_plz'
    return render(request, 'about.html',
                {'username' : username
                 })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects' : projects})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks' : tasks
    })

def create_task(request):
    print(request.GET['title'])
    print(request.GET['description'])
    Task.objects.create(title=request.GET['title'],
                        description=request.GET['description'], project_id=2)
    return render(request, 'create_task.html', {'form': CreateNewTask()})