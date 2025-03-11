from django.contrib import admin
from .models import News, Memoir, BlogPost, NewsCategory, MemoirCategory, BlogCategory

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(MemoirCategory)
class MemoirCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'source', 'created_at')
    list_filter = ('category', 'created_at', 'tags')
    search_fields = ('title', 'content', 'source')

@admin.register(Memoir)
class MemoirAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at', 'tags')
    search_fields = ('title', 'content')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at', 'tags')
    search_fields = ('title', 'content')