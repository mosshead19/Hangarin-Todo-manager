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

from hangarinorg.views import (TaskListView,SubtaskCreateView)
from hangarinorg import views


from django.contrib import admin
from django.urls import path
from hangarinorg import views 
 # or wherever your views are

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TaskListView.as_view(), name='dashboard'),  # Your existing home
    path('category/<int:category_id>/tasks/', views.CategoryTaskListView.as_view(), name='category_tasks'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),

    #create subtask view for dropdown for categories
    path('subtask/create/', views.SubtaskCreateView.as_view(), name='subtask_create'),
   
]