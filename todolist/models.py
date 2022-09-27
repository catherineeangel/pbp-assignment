from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)  # menambahkan created at timestamp scr otomatis, gbs di override
    title = models.CharField(max_length=255)
    description = models.TextField()