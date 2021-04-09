from django.shortcuts import render
from rest_framework import generics
from api import serializers
from django.contrib.auth.models import User
from .models import Post,comment
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=serializers.PostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    search_fields=('title','owner')
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=serializers.PostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class CommentList(generics.ListCreateAPIView):
    queryset=comment.objects.all()
    serializer_class=serializers.CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self,serializer):
        serializer.save(self.request.User)
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=comment.objects.all()
    serializer_class=serializers.CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializer
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializer
