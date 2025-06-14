from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to="post_images/")
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField()
    is_active = models.BooleanField(default=True)