from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .seralizers import PostSerializers


class PostListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializers(post, many=True)
        return Response(serializer.data)


class PostCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        if "image" in data.keys():
            image = data("image")
        else:
            image = None

        Post.objects.create(
            title=data["title"],
            content=data["content"],
            image=data["image"],
            user=request.user
        )
        return Response({"post": "created"}, status=201)


class PostUpdateAPIView(APIView):
    def put(self, request):
        pk = request.data["pk"]
        if not pk:
            return Response({"error": "pk is not required"}, status=404)
        try:
            instance = Post.objects.get(id=pk)

        except:
            return Response({"error": "object does not exists"})
        if request.user == instance.user:
            serializer = PostSerializers(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"post": serializer.data})




class PostDestroyAPIView(APIView):
    def delete(self, request):
        pk = request.data["pk"]
        if not pk:
            return Response({"error": "pk is not required"}, status=404)
        try:
            instance = Post.objects.get(id=pk)
            instance.dalete()
        except:
            if request.user == instance.user:
                return Response({"error": "object does not exists"})
        return Response({"post": f"post with id = {pk} deleted"})


class PostRetrieveAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        post = Post.objects.get(id=request.data["pk"])
        serializer = PostSerializers(post)
        return Response(serializer.data)






    # def get(self, request, *args, **kwargs):
    #     qs = Post.objects.all()
    #     serializer = PostSerializers(qs, many=True)
    #     return Response(serializer.data)