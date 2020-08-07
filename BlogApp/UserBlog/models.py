from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    image = models.ImageField(blank=True, upload_to='profile')


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(TimeStamp):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='blog')
    content = models.TextField()

    def __str__(self):
        return self.title
