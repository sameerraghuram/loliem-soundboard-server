from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=100, null=True, blank=True)
    clips = models.ManyToManyField(to='clips.AudioClip', related_name='clip_users', through='accounts.UserClip')


class UserClip(models.Model):
    user = models.ForeignKey('accounts.User', related_name='user_clips', on_delete=models.CASCADE)
    clip = models.ForeignKey('clips.AudioClip', on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
