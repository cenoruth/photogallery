from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    submitter = models.TextField(default='anonymous')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    uploaded_time = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.image