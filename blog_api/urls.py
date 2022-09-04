from django.urls import path
from .views import PostList, PostDetail, PostDetailFilter
from rest_framework import routers

app_name = "blog_api"

# router = routers.DefaultRouter()
# router.register('', PostList, basename='user')

# urlpatterns = router.urls
urlpatterns = [
    path('posts/<str:pk>', PostDetail.as_view(), name='detailpost'),
    path('search/', PostDetailFilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
    # path()
]
