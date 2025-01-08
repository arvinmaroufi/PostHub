from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'views', 'created_at', 'is_recommended', 'status']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['status']
    search_fields = ['title']
    list_editable = ['is_recommended', 'status']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'body', 'parent', 'created_at', 'active']
    list_editable = ['active']
    list_filter = ['active']

