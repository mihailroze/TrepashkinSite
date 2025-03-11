from django.db import models
from taggit.managers import TaggableManager

class NewsCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"

class MemoirCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория мемуаров"
        verbose_name_plural = "Категории мемуаров"

class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория блога"
        verbose_name_plural = "Категории блога"

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    tags = TaggableManager(blank=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Memoir(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='memoirs_images/', blank=True, null=True)
    tags = TaggableManager(blank=True)
    category = models.ForeignKey(MemoirCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    tags = TaggableManager(blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title