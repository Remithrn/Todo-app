from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=122)
    priority=models.IntegerField()
    date=models.DateField()

    def __str__(self) -> str:
        return self.name