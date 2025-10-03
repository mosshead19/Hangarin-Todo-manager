from django.shortcuts import render
from django.views.generic import ListView, CreateView  # Fixed import
from django.views.generic.edit import UpdateView, DeleteView  # Alternative
from django.urls import reverse_lazy
from hangarinorg.models import Task, Category

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryTaskListView(ListView):
    model = Task
    template_name = 'category_tasks.html'  # Simple path
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(category_id=self.kwargs['category_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = Category.objects.get(id=self.kwargs['category_id'])
        return context

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context