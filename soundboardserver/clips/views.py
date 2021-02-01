from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils import timezone
from django.views.generic import ListView, DetailView

from soundboardserver.accounts.models import User
from soundboardserver.clips.models import AudioClip


class AudioClipListView(ListView):
    model = AudioClip

    def get_queryset(self):
        self.user = get_object_or_404(User, name=self.kwargs['user_id'])
        return self.user.clips.all()


class AudioClipDetailView(DetailView):
    model = AudioClip
    queryset = AudioClip.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj
