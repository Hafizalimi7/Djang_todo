from django.urls import path
from .views import Index, AddTask, UpdateTask, UserOwnList, DeleteTask

app_name = "todo"

urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('add', AddTask.as_view(), name="add"),
    path('update/<int:pk>/', UpdateTask.as_view(), name="update"),
    path('user/<int:pk>', UserOwnList.as_view(), name="solo" ),
    path('delete/<int:pk>', DeleteTask.as_view(), name="delete" ),

]
