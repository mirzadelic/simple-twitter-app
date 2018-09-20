from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    ''' Post ModelSerializer
    '''

    class Meta:
        model = Post
        fields = ('id', 'name', 'content', 'created_at')
