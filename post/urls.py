from django.urls import path
from .views import (
    PostListAPIView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostDestroyAPIView,
    PostRetrieveAPIView,
)


urlpatterns = [
    path('api/', PostListAPIView.as_view(), name='list-post'),
    path('api/create/', PostCreateAPIView.as_view(), name='create-post'),
    path('api/update/', PostUpdateAPIView.as_view(), name='update-post'),
    path('api/delete/', PostDestroyAPIView.as_view(), name='destroy-post'),
    path('api/detail/', PostRetrieveAPIView.as_view(), name='retrieve-post'),
]
