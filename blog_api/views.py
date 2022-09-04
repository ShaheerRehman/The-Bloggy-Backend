from django.db.models.query import EmptyQuerySet
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AnonymousUser
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


# class PostList(ModelViewSet):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer
#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         if type(self.request.user) != AnonymousUser:
#             return get_object_or_404(Post.objects.filter(author=self.request.user), slug=item)
#     def get_queryset(self):
#         if type(self.request.user) != AnonymousUser:
#             user = self.request.user
#             return Post.objects.filter(author=user)
class PostList(generics.ListAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #
    # def get_queryset(self):
    #     if type(self.request.user) != AnonymousUser:
    #         user = self.request.user
    #         return Post.objects.filter(author=user)
    #     else:
    #         return Post.objects.none()


# class PostDetail(generics.ListAPIView):
#     # permission_classes = [PostUserWritePermission]
#     # queryset = Post.objects.filter(slug=)
#     serializer_class = PostSerializer
#
#     def get_object(self, queryset=None, **kwargs):
#
#         item = self.kwargs.get('pk')
#         if type(self.request.user) != AnonymousUser:
#             return get_object_or_404(Post.objects.filter(author=self.request.user), slug=item)
#     def get_queryset(self):
#         slug = self.request.query_params.get('slug', None)
#         return Post.objects.filter(slug=slug)
class PostDetail(generics.RetrieveAPIView):
    # permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    # queryset = Post.objects.filter(slug="pk")
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):


        item = self.kwargs.get('pk')
        return get_object_or_404(Post.objects.filter(slug=item))
    # def get_queryset(self):
    #
    #     item = self.kwargs.get('pk')
    #     print(item)
    #     return Post.objects.filter(slug=item)
        # return get_object_or_404(Post.objects.filter(author=self.request.user), slug=item)
    # def get_queryset(self):
    #     slug = self.request.query_params.get('slug', None)
    #     return Post.objects.filter(slug=slug)
# class PostDetail(generics.RetrieveAPIView):
#     # permission_classes = [AllowAny]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostDetailFilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AdminPostDetail(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class DeletePost(generics.DestroyAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer