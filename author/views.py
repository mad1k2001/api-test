from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import Post
from .seralizers import UserSerializers
from post.seralizers import PostSerializers


class UserAPIView(APIView):
    def get(self, request):
        user = User.objects.all()
        return Response({'USER': UserSerializers(user, many=True).data})


class UserRetrieveAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        user = User.objects.get(id=request.data["pk"])
        serializer = UserSerializers(user)
        return Response(serializer.data)


class UserListRetrieveAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        user = User.objects.get(id=request.data["pk"])
        post = Post.objects.filter(user=user)

        serializer = UserSerializers(user)
        if not user:
            return Response({'error': "user does not exist"})
        else:
            return Response({
                "user": serializer.data,
                "posts of this user":  PostSerializers(post,  many=True).data})


