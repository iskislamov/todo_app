from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Task
from .forms import RegisterForm

def index(request):
    num_tasks = Task.objects.all().count()
    num_initial_tasks = Task.objects.filter(status__exact='i').count()
    num_pending_tasks = Task.objects.filter(status__exact='p').count()
    num_resolved_tasks = Task.objects.filter(status__exact='r').count()

    return render(
        request,
        'index.html',
        context = {
            'num_tasks': num_tasks,
            'num_initial_tasks': num_initial_tasks,
            'num_pending_tasks': num_pending_tasks,
            'num_resolved_tasks': num_resolved_tasks
        }
    )

class TaskDetailView(generic.DetailView):
    model = Task

class InitialTasksPerUserListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'todo/task_initial_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user).filter(status__exact='i')

class PendingTasksPerUserListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'todo/task_pending_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user).filter(status__exact='p')

class ResolvedTasksPerUserListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'todo/task_resolved_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user).filter(status__exact='r')

class AllTasksPerUserListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'todo/task_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user)

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    initial = {'status': 'i', }

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'todo/task_update_form.html'
    fields = ['task_name', 'task_description', 'status', 'creator']

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('index')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            response = HttpResponse()
            response['user'] = user
            return response
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def test(request):
    return HttpResponse('This is test page!')