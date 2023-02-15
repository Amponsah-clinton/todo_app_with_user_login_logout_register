from django.db import models

# Create your models here.
class  myapp(models.Model):
    todo = models.CharField(max_length=200)
    date = models.DateField()
    
    def __str__(request):
        return request.todo
    
    
    