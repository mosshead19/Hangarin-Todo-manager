from django.shortcuts import render
from django.views.generic.list import ListView
from hangarinorg.models import Task,Category

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context