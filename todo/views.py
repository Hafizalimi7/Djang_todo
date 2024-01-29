from django.shortcuts import render , redirect, reverse
from django.views.generic import TemplateView, UpdateView, CreateView, ListView 
from .models import TodoMod
from django.urls import reverse_lazy

# Create your views here.
class Index(ListView):
  template_name = "base.html"
  queryset = TodoMod.objects.filter(completed=True)
  todo_names = TodoMod.objects.values_list('completed', flat=True)

  print(todo_names)
  context_object_name = "todo_list"

class AddTask(CreateView):
  model = TodoMod
  fields = ['name','task']
  template_name = "base.html"
  success_url = reverse_lazy("todo:home")
  

class UpdateTask(UpdateView):
  model = TodoMod
  fields = ['completed']
  template_name = "base.html"
  success_url = reverse_lazy("todo:home")
  # def get_queryset(self):
  #   query_set = TodoMod.objects.filter(completed=True, pk=self.kwargs['pk'])
  #   print("2", query_set)
  #   return query_set 
    

  
      
  
  
 
  
 
  
    


   
