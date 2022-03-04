from django.contrib import admin

from .models import Article, Scopes, ScopesArtical


class ScopesArticalInline(admin.TabularInline):
    model = ScopesArtical


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopesArticalInline]


@admin.register(Scopes)
class ScopesAdmin(admin.ModelAdmin):
    inlines = [ScopesArticalInline,]