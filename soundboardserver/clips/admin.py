from django.contrib import admin

# Register your models here.
from soundboardserver.clips.models import AudioClip


@admin.register(AudioClip)
class AudioClipAdmin(admin.ModelAdmin):
    pass
