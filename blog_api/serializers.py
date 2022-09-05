from blog.models import Post
from rest_framework import serializers
from blog.models import Category




class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    print(category_name)
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'image', 'slug', 'category_name', 'excerpt', 'content', 'status', )
