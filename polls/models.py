from django.db import models
from datetime import datetime
# Create your models here.

class AuthorModel(models.Model):
    name = models.CharField(default='',max_length=100)
    birthday = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name