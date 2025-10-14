from django.shortcuts import render
from django.views.generic import ListView, CreateView  # Fixed import
from django.views.generic.edit import  UpdateView, DeleteView  # Alternative
from django.urls import reverse_lazy
from hangarinorg.models import Task, Category, Subtask, Priority,Note
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
    template_name = 'task_form.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['priorities'] = Priority.objects.all()
        context['notes'] = Note.objects.filter(task=self.object).order_by('-created_at')
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Check if this is a note creation request
        if 'add_note' in request.POST and 'note_content' in request.POST:
            # Create a new note
            Note.objects.create(
                content=request.POST['note_content'],
                task=self.object
            )
            # Redirect back to the same task edit page
            return redirect('task-update', pk=self.object.pk)
        
        # Otherwise, handle the normal task update
        return super().post(request, *args, **kwargs)

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['priorities'] = Priority.objects.all()
        return context
    
  #TASK CRUD VIEWS  
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
    template_name = 'index.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['priorities'] = Priority.objects.all()
        context['tasks'] = Task.objects.all()
        context['notes'] = Note.objects.all()
        return context
    
    def form_invalid(self, form):
        # If form is invalid, return to same page with errors
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
    template_name = 'task_form.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['priorities'] = Priority.objects.all()
        context['notes'] = Note.objects.filter(task=self.object).order_by('-created_at')
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Check if this is a note creation request
        if 'add_note' in request.POST and 'note_content' in request.POST:
            # Create a new note
            Note.objects.create(
                content=request.POST['note_content'],
                task=self.object
            )
            # Redirect back to the same task edit page
            return HttpResponseRedirect(reverse_lazy('task-update', kwargs={'pk': self.object.pk}))
        
        # Otherwise, handle the normal task update
        return super().post(request, *args, **kwargs)

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
        context['priorities'] = Priority.objects.all()
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
    ordering = ['-created_at']  # Show newest first
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # For your sidebar
        return context
    
class NoteCreateView(CreateView):
    model = Note
    fields = ['content']
    template_name = 'note_form.html'
    success_url = reverse_lazy('task-update')     
    
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
    

