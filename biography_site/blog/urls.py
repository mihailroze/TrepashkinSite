from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('memoirs/', views.memoirs_list, name='memoirs_list'),
    path('memoirs/<int:memoir_id>/', views.memoir_detail, name='memoir_detail'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('memoirs/category/<int:category_id>/', views.memoirs_by_category, name='memoirs_by_category'),
]