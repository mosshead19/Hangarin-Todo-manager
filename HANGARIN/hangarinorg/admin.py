from django.contrib import admin

from .models import Category, Note, Priority, Subtask, Task

class SubTaskInline(admin.TabularInline):
    model = Subtask
    extra = 1
    fields = ("title", "status")
    show_change_link = True

class NoteInline(admin.StackedInline):
    model = Note
    extra = 1
    fields = ("content", "created_at")
    readonly_fields = ("created_at",)
    

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','deadline',  'priority', 'category')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('title', 'description')

    inlines = [SubTaskInline, NoteInline]
    
    
@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'parent_task')
    list_filter = ('status',)
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('task', 'content','created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)


