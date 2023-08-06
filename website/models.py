from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class New(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default = "placeholder")
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices = STATUS, default=0)

    class Meta:
        ordering = ['-date_created']
        
    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg', upload_to='user_pictures')
