from django.db import models
from datetime import date, timedelta


class User(models.Model):
    fname = models.CharField(max_length=255)
    password = models.CharField(max_length=200)
 
class Todo(models.Model):
    todo_job= models.TextField()
    user=models.ForeignKey('User')
    due_date=models.DateField()
    status = models.CharField(max_length=10,default = 'Pending')
    def is_due(self):
        if date.today()<=self.due_date:
            return True
        return False
