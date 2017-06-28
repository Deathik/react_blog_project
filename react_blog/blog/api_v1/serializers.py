from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ('url', 'id', 'author', 'title',
                  'text', 'pub_date', 'last_modified')


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True,
                                                view_name='post-detail',
                                                read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'posts')
