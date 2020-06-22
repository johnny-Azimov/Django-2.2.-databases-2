from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Theme, ArticleTheme


class ArticleThemeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            try:
                if form.cleaned_data['is_main']:
                    count += 1
            except KeyError:
                pass
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if count > 1:
            raise ValidationError('Должна быть только одна основная тема')
        else:
            return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleThemeInline(admin.TabularInline):
    model = ArticleTheme
    formset = ArticleThemeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleThemeInline]


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    inlines = [ArticleThemeInline]