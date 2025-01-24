from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at', 'due_date', 'priority')
    list_filter = ('is_completed', 'created_at', 'due_date', 'priority')
    search_fields = ('title', 'description')
    
admin.site.register(Task, TaskAdmin)