from django.db import models

from catagories.models import Catagory
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    catagroy = models.ManyToManyField(Catagory)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
