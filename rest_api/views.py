from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from post.models import Post
from .serializers import PostSerializer
# Create your views here.

class postList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class postDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer