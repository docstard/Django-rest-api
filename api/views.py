
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.fields import REGEX_TYPE
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from .models import User_api

from .filters import UserFilter
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/user-list/',
        'show':'/show table of users/',
    }

    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    users = User_api.objects.all()
    serializer = UserSerializer(users, many= True)
    return Response(serializer.data)

def userData(request):
    user = User_api.objects.all()

    # orders = user.order_set.all()
    # order_count = orders.count()

    myFilter = UserFilter(request.GET, queryset=user)
    user = myFilter.qs

    param = {'user':user,'orders':user,'myFilter':myFilter}
    return render(request, 'api/user.html',param)