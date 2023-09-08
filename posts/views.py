from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class PostAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()