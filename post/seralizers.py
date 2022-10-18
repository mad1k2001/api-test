from django.contrib.auth.models import User
from rest_framework import serializers
from author.seralizers import UserSerializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)

    class Meta:
         model = Post
         fields = ['id', 'user', 'title', 'content', 'image']
         read_only_fields = ['user']

