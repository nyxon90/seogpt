# Generated by Django 4.2.5 on 2023-09-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copywriting', '0008_alter_config_promt_items'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='config',
            options={'verbose_name': 'Конфигурация', 'verbose_name_plural': 'Конфигурация'},
        ),
        migrations.AlterField(
            model_name='config',
            name='promt_article',
            field=models.TextField(verbose_name='Промт для получения текста'),
        ),
        migrations.AlterField(
            model_name='config',
            name='promt_items',
            field=models.TextField(verbose_name='Промт для получения списка статей'),
        ),
    ]
