# Generated by Django 4.2.5 on 2023-09-23 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('copywriting', '0002_alter_articles_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='kewords',
            new_name='keywords',
        ),
    ]