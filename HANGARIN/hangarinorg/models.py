from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):  
        return self.name
    
class Category(BaseModel):
    name = models.CharField(max_length=100)

   
    def __str__(self):
        return self.name

class Task(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
    max_length=50, choices = [    ("Pending","Pending"), 
         ("In Progress","In Progress"),      ("Completed","Completed")       ], default="Pending")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title
    



class Note(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()

    def __str__(self):
        return f"Note for Task: {self.task.title}"
    

class Subtask(BaseModel):
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=200)
    status = models.CharField(
    max_length=50, choices = [    ("Pending","Pending"), 
         ("In Progress","In Progress"), ("Completed","Completed")], default="Pending")
    
    def __str__(self):
        return self.title
    
    

