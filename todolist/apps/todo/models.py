from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Task(models.Model):
    task_name = models.CharField('Task name', help_text='Enter name of the task', max_length=30)
    task_description = models.TextField('Task description', help_text='Add task description', max_length=200)

    TASK_STATUS = (
        ('i', 'Initial'),
        ('p', 'Pending'),
        ('r', 'Resolved')
    )

    status = models.CharField(max_length=1, choices=TASK_STATUS, default='i', help_text='Set status of the task')

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.id)])
