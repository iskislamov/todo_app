from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('initial/', views.InitialTasksPerUserListView.as_view(), name='initial'),
    path('pending/', views.PendingTasksPerUserListView.as_view(), name='pending'),
    path('resolved/', views.ResolvedTasksPerUserListView.as_view(), name='resolved'),
    path('all/', views.AllTasksPerUserListView.as_view(), name='all'),
    path('task/(?P<pk>\d+)', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/create/', views.TaskCreate.as_view(), name='task_create'),
    path('task/(?P<pk>\d+)/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('task/(?P<pk>\d+)/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('test/', views.test, name = 'test'),
    path('register/', views.register, name='register')
]
