from django.db import models


class Post(models.Model):
    ''' Post Model
    '''
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-created_at',)
