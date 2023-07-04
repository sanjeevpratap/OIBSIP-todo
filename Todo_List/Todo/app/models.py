from django.db import models

class Task(models.Model):
    Title=models.CharField(max_length=30, null=True)
    Desc=models.TextField()
    Time=models.DateTimeField(auto_now_add=True)
    dead=models.DateField()

    def __str__(self):
        return self.Title+"  "+self.Time
