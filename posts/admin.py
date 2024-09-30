from django.contrib import admin
from pip._vendor.rich.markup import Tag

from posts.models import Post, Category, tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'rate','crated_at', 'updated_at')
    list_display_links = ('title','content', 'rate','crated_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'category', 'tags')
    list_editable = ('rate')
    list_per_page = 2
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name")
    list_display_links = ("name")

@admin.register(tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name")
    list_display_links = ("name")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "post")
    list_display_links = ("text", "post")