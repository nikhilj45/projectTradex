from django.db import models
from django.contrib.auth.models import User

class posts(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    text       = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return self.user.username
