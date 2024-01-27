from django.urls import path
from .views import Index, AddTask, UpdateTask

app_name = "todo"

urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('add', AddTask.as_view(), name="add"),
    path('update/<int:pk>/', UpdateTask.as_view(), name="update_todo"),
]
