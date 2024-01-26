from django.shortcuts import render , redirect
from django.views.generic import TemplateView, UpdateView, CreateView
from .models import TodoMod
from django.urls import reverse_lazy

# Create your views here.
class Index(TemplateView):
  template_name = "base.html"

class AddTask(CreateView):
  template_name = "base.html"
  model = TodoMod
  fields = ['task']
  success_url = "index"
  
  def add(request):
    task = request.POST["task"]
    todo = TodoMod(task=task)
    print("dgfdfs")
    todo.save()
    print("SAVEDDDD")
    


   
