from django.db import models


class Theme(models.Model):
    title = models.CharField(max_length=256, verbose_name='Тема')

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    themes = models.ManyToManyField(
        Theme,
        through='ArticleTheme',
        through_fields=('article', 'theme'),
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.title}'


class ArticleTheme(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основная тема', default=False)

    def __str__(self):
        return f'{self.article}{self.theme}{self.is_main}'
