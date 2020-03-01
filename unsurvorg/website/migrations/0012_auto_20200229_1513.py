# Generated by Django 2.2.10 on 2020-02-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20200228_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.TextField(blank=True, max_length=360),
        ),
        migrations.AlterField(
            model_name='article',
            name='publication_datetime',
            field=models.DateTimeField(verbose_name='date_published'),
        ),
        migrations.AlterField(
            model_name='translatedarticle',
            name='abstract',
            field=models.TextField(blank=True, max_length=360),
        ),
        migrations.AlterField(
            model_name='translatedarticle',
            name='publication_datetime',
            field=models.DateTimeField(verbose_name='date_published'),
        ),
    ]
