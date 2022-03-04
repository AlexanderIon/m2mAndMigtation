from django.shortcuts import render

from articles.models import Article, ScopesArtical


def articles_list(request):
    template = 'articles/news.html'
    articals = Article.objects.all()
    context = {'object_list': articals}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)


def all_view(request):
    template = 'articles/probnic.html'
    articals = Article.objects.all()
    context = {'articles': articals}
    scope = ScopesArtical.objects.all()
    for s in scope:
        print(f"Статья:{s.art}: сфера {s.scopes}: main {s.main}")
    return render(request,template,context)