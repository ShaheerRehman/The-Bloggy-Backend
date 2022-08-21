from django.urls import path
from .views import PostList
from rest_framework import routers

app_name = "blog_api"

router = routers.DefaultRouter()
router.register('', PostList, basename='user')

urlpatterns = router.urls
