from django.shortcuts import render, get_object_or_404
from .models import News, Memoir, BlogPost, NewsCategory, MemoirCategory, BlogCategory

def news_list(request):
    news = News.objects.all().order_by('-created_at')
    categories = NewsCategory.objects.all()
    return render(request, 'blog/news_list.html', {'news': news, 'categories': categories})

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'blog/news_detail.html', {'news': news})

def news_by_category(request, category_id):
    news = News.objects.filter(category_id=category_id).order_by('-created_at')
    categories = NewsCategory.objects.all()
    selected_category = NewsCategory.objects.get(id=category_id)
    return render(request, 'blog/news_list.html', {'news': news, 'categories': categories, 'selected_category': selected_category})

def memoirs_list(request):
    memoirs = Memoir.objects.all().order_by('-created_at')
    categories = MemoirCategory.objects.all()
    return render(request, 'blog/memoirs_list.html', {'memoirs': memoirs, 'categories': categories})

def memoir_detail(request, memoir_id):
    memoir = get_object_or_404(Memoir, id=memoir_id)
    return render(request, 'blog/memoir_detail.html', {'memoir': memoir})

def memoirs_by_category(request, category_id):
    memoirs = Memoir.objects.filter(category_id=category_id).order_by('-created_at')
    categories = MemoirCategory.objects.all()
    selected_category = MemoirCategory.objects.get(id=category_id)
    return render(request, 'blog/memoirs_list.html', {'memoirs': memoirs, 'categories': categories, 'selected_category': selected_category})

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    categories = BlogCategory.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts, 'categories': categories})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})

def blog_by_category(request, category_id):
    posts = BlogPost.objects.filter(category_id=category_id).order_by('-created_at')
    categories = BlogCategory.objects.all()
    selected_category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/blog_list.html', {'posts': posts, 'categories': categories, 'selected_category': selected_category})