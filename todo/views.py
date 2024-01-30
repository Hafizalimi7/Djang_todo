from django.shortcuts import reverse
from django.views.generic import UpdateView, CreateView, ListView, DetailView, DeleteView
from .models import TodoMod
from django.urls import reverse_lazy

# Create your views here.
class Index(ListView):
  template_name = "base.html"
  queryset = TodoMod.objects.all()
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
  
class UserOwnList(DetailView):
  model = TodoMod
  template_name = "selftask.html"
  
  def get_success_url(self):
    pk_value = self.object.pk
    return reverse("todo:solo", kwargs={'pk': pk_value})

class DeleteTask(DeleteView):
  model = TodoMod
  template_name = "base.html"
  fields = "__all__"  
  success_url = reverse_lazy("todo:home")
 

  
      
  
  
 
  
 
  
    


   
