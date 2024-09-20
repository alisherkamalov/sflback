from django.db import models
# Create your models here.

class CustomAccount(models.Model):
    name = models.CharField(max_length=200)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)