from django.db import models

# Create your models here.
class TodoMod(models.Model):
  name = models.CharField(max_length=100)
  task = models.CharField(max_length=5000)
  completed = models.BooleanField(default=False)
  
  def __str__(self) -> str:
    return self.name