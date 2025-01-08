from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Article, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def get_pages_to_show(current_page, total_pages):
    """Utility function to determine which pagination pages to show."""
    if total_pages <= 3:
        return list(range(1, total_pages + 1))

    if current_page <= 2:
        return [1, 2, 3, '...', total_pages]

    if current_page >= total_pages - 1:
        return [1, '...', total_pages - 2, total_pages - 1, total_pages]

    return [1, '...', current_page - 1, current_page, current_page + 1, '...', total_pages]


def home(request):
    popular_article = Article.objects.filter(status='published').order_by('-views')[:3]
    latest_article = Article.objects.filter(status='published').order_by('created_at')[:6]
    recommended_articles = Article.objects.filter(status='published', is_recommended=True).order_by('-created_at')[:3]
    return render(request, 'blog/home.html', {'popular_article': popular_article, 'latest_article': latest_article,
                                              'recommended_articles': recommended_articles})


def article_detail(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    recommended_articles = Article.objects.filter(status='published', is_recommended=True).exclude(id=articles.id).order_by('-created_at')[:3]
    articles.views += 1
    articles.save()
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=articles, user=request.user, parent_id=parent_id)
    return render(request, 'blog/article_detail.html', {'articles': articles, 'recommended_articles': recommended_articles,
                                                        'current_article': articles})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    comment.delete()
    return redirect('blog:article_detail', slug=comment.article.slug)


def article_list(request):
    articles = Article.objects.filter(status='published')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    return render(request, 'blog/articles_list.html', {'articles': object_list, 'pages_to_show': pages_to_show})


def category_article(request, slug):
    category_list = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(status='published', category=category_list)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    return render(request, 'blog/category_article.html', {'category_list': category_list, 'articles': object_list,
                                                          'pages_to_show': pages_to_show})


def search(request):
    search_article = request.GET.get('search')
    articles = Article.objects.filter(title__icontains=search_article, status='published')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)
    return render(request, 'blog/articles_list.html', {'articles': object_list, 'pages_to_show': pages_to_show})


def about(request):
    return render(request, 'blog/about_me.html')
