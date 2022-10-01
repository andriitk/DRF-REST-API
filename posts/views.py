from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework import viewsets
from .permissions import *
from .models import Post
from .serializers import *


# class PostList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     permission_classes = (IsAuthorOrReadOnly, permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView):  # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):  # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# Что бы не повторяться заменим 4 вбюхи двумя сетами
class PostViewSet(viewsets.ModelViewSet):  # new
    permission_classes = (IsAuthorOrReadOnly, permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):  # new
    permission_classes = (IsPermissionForUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
