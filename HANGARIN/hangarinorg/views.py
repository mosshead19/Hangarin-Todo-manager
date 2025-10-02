from django.shortcuts import render
from django.views.generic.list import ListView
from hangarinorg.models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'