# Generated by Django 2.2.10 on 2020-02-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_article_keep_top_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='last_updated_date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='article',
            name='last_updated_datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='last_updated'),
        ),
        migrations.AddField(
            model_name='article',
            name='publication_datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]
