import requests
from dateutil import parser, tz
from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import viewsets


from .serializers import UserSerializer, GroupSerializer


def handle_datetime(date):
    to_zone = tz.tzlocal()
    time = parser.parse(date).replace().astimezone(to_zone)
    return time

def home(request):
    if request.POST:
        print(request.POST.items)
    context = {'foo': 'foobar'}
    return render(request, '../templates/index.html', context)


def tests_page(request):
    if request.POST:
        print(request.POST.items)
    context = {'foo': 'foobar'}
    return render(request, '../templates/tests.html', context)


def results_page(request):
    if request.POST:
        print(request.POST.items)
    context = {'foo': 'foobar'}
    return render(request, '../templates/results.html', context)


# created for the purpose of adding endpoints for repurposing the data but i think that might be overkill for this task.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer