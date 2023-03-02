from django.contrib import admin
from . models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'status', 'created', 'publish')
    search_fields = ['title', 'body']
    list_editable = ['publish', 'status']
    date_hierarchy = 'publish'
    raw_id_fields = ('author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
