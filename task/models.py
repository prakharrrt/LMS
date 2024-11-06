from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name=models.CharField(null=False,blank=False,max_length=255)
    description=models.CharField(null=False,blank=False,max_length=255)
    author=models.CharField(null=False,blank=False,max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}--{self.name}--{self.status}'
