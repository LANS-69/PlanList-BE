# Generated by Django 5.1.3 on 2024-11-24 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planlist', '0002_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='storeUrl',
            field=models.URLField(blank=True, max_length=2000),
        ),
    ]
