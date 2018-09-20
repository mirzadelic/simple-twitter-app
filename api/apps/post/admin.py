from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    ''' Post Admin
    '''

    search_fields = ('name', 'content')
    list_filter = readonly_fields = ('created_at',)
    list_display = list_display_links = ('name', 'content', 'created_at')


admin.site.register(Post, PostAdmin)
