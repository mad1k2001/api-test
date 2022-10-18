from django.urls import path
from .views import (
    UserAPIView,
    UserRetrieveAPIView,
    UserListRetrieveAPIView,
)


urlpatterns = [
    path('api/list/', UserAPIView.as_view(), name='list-post'),
    path('api/retrieve/', UserRetrieveAPIView.as_view(), name='retrieve-post'),
    path('api/userlist/', UserListRetrieveAPIView.as_view(), name='users-post')
]
