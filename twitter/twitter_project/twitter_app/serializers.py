from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'email',)


class TweetSerializers(serializers.ModelSerializer):
    class Meta:
        username = UserSerializers()
        model = Tweet
        fields = ('id', 'tweet', 'post', 'user_name', 'update_post', 'delete_post')