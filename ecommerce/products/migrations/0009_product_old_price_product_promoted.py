# Generated by Django 4.1.1 on 2022-09-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_midcategory_category_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='promoted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
