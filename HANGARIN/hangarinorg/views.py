from django.shortcuts import render
from django.views.generic import ListView, CreateView  # Fixed import
from django.views.generic.edit import  UpdateView, DeleteView  # Alternative
from django.urls import reverse_lazy
from hangarinorg.models import Task, Category, Subtask, Priority,Note

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
  #TASK CRUD VIEWS  
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
    template_name = 'task_form.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
    template_name = 'task_form.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('dashboard')
    
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
    
# Category CRUD VIEWS
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    


#priority CRUD VIEWS 

class PriorityListView(ListView):
    model = Priority
    template_name = 'priority_list.html'
    context_object_name = 'priorities'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
class PriorityCreateView(CreateView):
    model = Priority
    fields = ['name']
    template_name = 'priority_form.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PriorityUpdateView(UpdateView):
    model = Priority
    fields = ['name']
    template_name = 'priority_form.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priority_confirm_delete.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
#note crush views

class NoteListView(ListView):
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
class NoteCreateView(CreateView):
    model = Note
    fields = ['content']
    template_name = 'note_form.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['content']
    template_name = 'note_form.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

#Subtask

class SubtaskListView(ListView):
    model = Subtask
    template_name = 'subtask_list.html'
    context_object_name = 'subtasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class SubtaskCreateView(CreateView):
    model = Subtask
    fields = ['title', 'status']
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('dashboard')  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class SubtaskUpdateView(UpdateView):
    model = Subtask
    fields = ['title', 'status']
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('dashboard')  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class SubtaskDeleteView(DeleteView):
    model = Subtask
    template_name = 'subtask_confirm_delete.html'
    success_url = reverse_lazy('dashboard')  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    

