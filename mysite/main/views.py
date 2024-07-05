from django.shortcuts import render, redirect

from .models import *
from .forms import *

# Create your views here.

def home(request):
    tasks = Tasks.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request, 'main/home.html', context={'tasks':tasks, 'form':form})
