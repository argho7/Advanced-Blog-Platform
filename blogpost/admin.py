from django.contrib import admin
from .models import Category, Tags, Post
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def thumbnail_view(self, obj):
        if obj.thumbnail:
            return mark_safe(f'<img src="{obj.thumbnail.url}" >')
        else:
            return 'Not Available'

    list_display = ('title', 'id', 'author', 'slug', 'category', 'status',
                    'visibility', 'created_at','updated_at', 'published_at')
    list_filter = ('status',  'visibility', 'category', 'tags','created_at',
                   'updated_at', 'published_at')
    search_fields = ('title', 'author', 'slug', 'content', 'category', 'tags',)
    readonly_fields = ('thumbnail_view',)
    
admin.site.register(Category)
admin.site.register(Tags)