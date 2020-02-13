# Generated by Django 2.2.10 on 2020-02-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200212_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low_res1', models.ImageField(blank=True, upload_to='images/low_res')),
                ('high_res1', models.ImageField(blank=True, upload_to='images/high_res')),
                ('low_res2', models.ImageField(blank=True, upload_to='images/low_res')),
                ('high_res2', models.ImageField(blank=True, upload_to='images/high_res')),
                ('article', models.ForeignKey(on_delete='CASCADE', related_name='images', to='website.Article')),
            ],
        ),
    ]
