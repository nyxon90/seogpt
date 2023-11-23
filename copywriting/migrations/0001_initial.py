# Generated by Django 4.2.5 on 2023-09-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(verbose_name='user_id')),
                ('status', models.TextField(verbose_name='Статус')),
                ('kewords', models.TextField(verbose_name='Ключевые слова')),
                ('structure', models.TextField(verbose_name='Содержание')),
                ('content', models.TextField(verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
