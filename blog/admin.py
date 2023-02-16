from django.contrib import admin
from . models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'status', 'created', 'publish')
    search_fields = ['title', 'body']
    list_editable = ['publish', 'status']
    date_hierarchy = 'publish'
    raw_id_fields = ('author',)