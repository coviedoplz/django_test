from django import forms

from myapp.models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))
    project = forms.ChoiceField(label="selecciona un proyecto", choices=Project.objects.all().values_list('id', 'name'))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto")   