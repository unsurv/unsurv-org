# Generated by Django 2.2.10 on 2020-02-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='keep_top_position',
            field=models.BooleanField(default=False),
        ),
    ]
