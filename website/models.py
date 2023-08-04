from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    dated_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)