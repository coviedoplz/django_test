from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import redirect, render, get_object_or_404
from .forms import CreateNewProject, CreateNewTask
from django.contrib import messages

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
    return render(request, 'projects/projects.html', {'projects' : projects})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks' : tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': CreateNewTask()})
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=request.POST['project'])
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form': CreateNewProject()})
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
                   'project':project,
                   'tasks': tasks})

def delete_task(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        task.delete()
        messages.success(request, 'Tarea eliminada correctamente')
        return redirect('tasks')

def update_status(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        task.done = True
        task.save()
        return redirect('tasks')
    else:
        return redirect('tasks')
    
