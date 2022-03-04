from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    #scope
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scopes(models.Model):

    text_scope = models.CharField(max_length=256)
    articals = models.ManyToManyField(Article, related_name='scope',through='ScopesArtical')
    #scopes

    def __str__(self):
        return self.text_scope



class ScopesArtical(models.Model):
    art = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='art')
    scopes = models.ForeignKey(Scopes, on_delete=models.CASCADE, related_name='scopes')
    main = models.BooleanField()






