from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer


class PostView(ModelViewSet):
    ''' Post ModelViewSet
        - url: /api/v1/post/post/
    '''

    queryset = Post.objects.all()
    serializer_class = PostSerializer
