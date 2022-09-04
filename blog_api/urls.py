from django.urls import path
from .views import PostList, PostDetail, PostDetailFilter, CreatePost, EditPost, DeletePost, AdminPostDetail
from rest_framework import routers

app_name = "blog_api"

# router = routers.DefaultRouter()
# router.register('', PostList, basename='user')

# urlpatterns = router.urls
urlpatterns = [
    path('posts/<str:pk>', PostDetail.as_view(), name='detailpost'),
    path('search/', PostDetailFilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/<int:pk>', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>', DeletePost.as_view(), name='deletepost'),
    path('admin/edit/postdetail/<int:pk>', AdminPostDetail.as_view(), name='admindetailpost'),
]
