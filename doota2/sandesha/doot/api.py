from .models import Post
from rest_framework import viewsets, permissions
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permissio_class = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer