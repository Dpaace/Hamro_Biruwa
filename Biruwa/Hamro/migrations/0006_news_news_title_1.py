# Generated by Django 4.0 on 2022-01-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hamro', '0005_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_title_1',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
