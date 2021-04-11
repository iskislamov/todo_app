from django.contrib import admin

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'creator', 'status')
    list_filter = ['status']

    fieldsets = (
        (None, {
            'fields': ('task_name', 'task_description')
        }),
        ('Availability', {
            'fields': ('status', 'creator')
        }),
    )