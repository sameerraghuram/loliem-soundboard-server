from django.contrib import admin

from soundboardserver.accounts.models import User, UserClip


class AudioClipInline(admin.TabularInline):
    model = UserClip


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [AudioClipInline]
