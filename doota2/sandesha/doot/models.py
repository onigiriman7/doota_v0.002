from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default="Enter Suitable Title")
    text = models.TextField(max_length=256, default="Write your post here...")

    def __str__(self):
        return self.title