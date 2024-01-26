from django.urls import path
from .views import Index, AddTask

app_name = "todo"

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('add', AddTask.as_view(), name="added_task")
   
]
