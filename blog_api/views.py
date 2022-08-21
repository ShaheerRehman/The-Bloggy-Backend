from django.shortcuts import get_object_or_404
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
# class PostList(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
