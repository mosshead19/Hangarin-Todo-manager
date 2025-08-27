from django.contrib import admin

from .models import Category, Note, Priority, Subtask, Task


admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Priority)
admin.site.register(Subtask)
admin.site.register(Task)