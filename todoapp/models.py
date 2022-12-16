from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class TodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(default=(timezone.now()+timezone.timedelta(days=7)).strftime("%Y.%m.%d-%H:%M:%S"))
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
