# Generated by Django 3.1.3 on 2020-12-01 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whats_free_on_craigslist_app', '0003_auto_20201201_0307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='post_title',
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_image_url',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_price',
            field=models.TextField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_title',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_url',
            field=models.TextField(default='', max_length=500),
        ),
    ]
