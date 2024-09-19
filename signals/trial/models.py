from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    background = models.CharField(max_length=225)

    def __str__(self):
        return self.user.username
