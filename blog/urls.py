from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:slug>/', views.article_detail, name='article_detail'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('articles/', views.article_list, name='article_list'),
    path('category/<slug:slug>/', views.category_article, name='category_article'),
    path('search/', views.search, name='search_article'),
    path('about/', views.about, name='about'),
]
