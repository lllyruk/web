from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task
# Create your views here.


def index(request):
    return render(request, 'web/index.html', {'title':'Nut Paradise'})


def about(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'web/about.html',{'title':'О нас','tasks': tasks})


def katalog(request):
    return render(request, 'web/katalog.html',{'title':'Каталог'})


def login(request):
    return render(request , 'web/login.html',{'title':'Вход'})

def contact(request):
    return render(request, 'web/contact.html',{'title':'Контакты'})


def create_about(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')

    form = TaskForm()
    context={
        'form':form
    }
    return render(request, 'web/create_about.html',context)
