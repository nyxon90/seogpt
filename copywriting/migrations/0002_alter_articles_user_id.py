# Generated by Django 4.2.5 on 2023-09-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copywriting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='user_id',
            field=models.IntegerField(verbose_name='user_id'),
        ),
    ]
