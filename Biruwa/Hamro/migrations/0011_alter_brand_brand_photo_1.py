# Generated by Django 4.0 on 2022-02-02 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hamro', '0010_rename_brand_photo1_brand_brand_photo_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
