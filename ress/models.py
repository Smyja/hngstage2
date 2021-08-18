from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True) 
 
    
    def __str__(self):
        return f"{self.email}"
        