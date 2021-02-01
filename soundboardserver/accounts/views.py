from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets

from soundboardserver.accounts.models import User
from soundboardserver.accounts.serializers import UserSerializer


def user_info(request):
    return HttpResponse("<h1>Good one</h1>")


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
