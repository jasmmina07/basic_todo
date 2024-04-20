from django.db import models

# Create your models here.

class Task(models.Model):
    id        = models.IntegerField()
    title     = models.CharField(max_length = 100)
    completed = models.DateTimeField(auto_now = True)
    created   = models.DateTimeField(auto_now = True)
    user_id   = models.IntegerField()

    def __str__(self) -> str:
        return self.title+" "+self.user_id
    