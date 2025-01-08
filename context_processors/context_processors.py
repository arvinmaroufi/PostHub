from blog.models import Article, Category


def default(request):
    latest_articles = Article.objects.filter(status='published').order_by('-created_at')[:4]
    categories = Category.objects.all()
    return {'latest_articles': latest_articles, 'categories': categories}
