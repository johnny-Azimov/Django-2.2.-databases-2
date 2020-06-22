# Generated by Django 3.0.6 on 2020-06-01 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название темы')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Theme')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='themes',
            field=models.ManyToManyField(through='articles.ArticleTheme', to='articles.Theme'),
        ),
    ]
