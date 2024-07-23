from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.PositiveIntegerField()
    disease = models.CharField(max_length=100, blank=True, null=True)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
