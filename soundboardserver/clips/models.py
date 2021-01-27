from django.db import models

# Create your models here.


class AudioClip(models.Model):
    CLIP_TYPE_YT = 'youtube'
    CLIP_TYPE_FILE = 'file'
    CLIP_TYPE_CHOICES = (
        (CLIP_TYPE_YT, 'YouTube Audio'),
        (CLIP_TYPE_FILE, 'Audio File'),
    )

    name = models.CharField(max_length=250)
    clip_type = models.CharField(choices=CLIP_TYPE_CHOICES, max_length=50, default=CLIP_TYPE_FILE)
    url = models.URLField(max_length=200)
    icon_url = models.CharField(max_length=250, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[CLIP] {name} {url}".format(name=self.name, url=self.url)
