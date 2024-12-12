from django.contrib import admin
from .models import BlogPost, Comment

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'main_content']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['content']

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)