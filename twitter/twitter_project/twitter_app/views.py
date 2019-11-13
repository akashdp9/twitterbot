from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from .models import *

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import viewsets,status
from .serializers import *


@api_view(['GET', ])
def api_user_list_view(request):
    user = User.objects.all()
    if request.method == 'GET':
        serializer = UserSerializers(user, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def api_user_id_list_view(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            serializer = UserSerializers(user)
            return Response(serializer.data)


@api_view(['GET', ])
def api_tweet_list_view(request):
    tweet = Tweet.objects.filter(delete_post=False)
    if request.method == 'GET':
        serializer = TweetSerializers(tweet, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def api_tweet_id_list_view(request, id):
    try:
        user = Tweet.objects.get(id=id, delete_tweet=False)
    except User.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            serializer = TweetSerializers(user)
            return Response(serializer.data)


@api_view(['POST', ])
def api_create_user_view(request):
    if request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['Success'] = 'Created Successfully'
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def api_create_tweet_view(request):
    if request.method == 'POST':
        print(request.data)
        serializer = TweetSerializers(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['Success'] = 'Created Successfully'
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def api_update_tweet_view(request, id):
    try:
        user = Tweet.objects.get(id=id, delete_post=False)
    except Tweet.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'PUT':
            serializer = TweetSerializers(user, data=request.data)
            if serializer.is_valid():
                data = {}
                serializer.save()
                data['Success'] = 'Updated Successfully'
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_406_NOT_ACCEPTABLE)
