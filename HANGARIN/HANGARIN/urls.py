"""
URL configuration for HANGARIN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from hangarinorg.views import (  TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    CategoryTaskListView, CategoryUpdateView, CategoryDeleteView, CategoryListView,
    PriorityCreateView, PriorityUpdateView, PriorityDeleteView,PriorityListView,
    SubtaskCreateView, SubtaskUpdateView, SubtaskDeleteView, SubtaskListView,
    NoteCreateView, NoteUpdateView, NoteDeleteView,NoteListView )
from hangarinorg import views

from django.contrib import admin
from django.urls import path
from hangarinorg import views 
 # or wherever your views are

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TaskListView.as_view(), name='dashboard'),#tasklist=dashboard  # Your existing home
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

   # Category URLs
   path('category/<int:category_id>/tasks/', views.CategoryTaskListView.as_view(), name='category_tasks'),
   
   path('categories/', CategoryListView.as_view(), name='category-list'), 
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
     path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

  # Priority URLs
  path('priorities/', PriorityListView.as_view(), name='priority-list'),
    path('priority/create/', PriorityCreateView.as_view(), name='priority-create'),
    path('priority/<int:pk>/edit/', PriorityUpdateView.as_view(), name='priority-update'),
    path('priority/<int:pk>/delete/', PriorityDeleteView.as_view(), name='priority-delete'),
    
   # Subtask URLs
   path('subtasks/', SubtaskListView.as_view(), name='subtask-list'), 
    path('subtask/create/', SubtaskCreateView.as_view(), name='subtask-create'),
    path('subtask/<int:pk>/edit/', SubtaskUpdateView.as_view(), name='subtask-update'),
    path('subtask/<int:pk>/delete/', SubtaskDeleteView.as_view(), name='subtask-delete'),
    
  
    # Note URLs
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('note/create/', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/edit/', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]