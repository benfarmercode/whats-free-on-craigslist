# Generated by Django 3.1.3 on 2020-12-02 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whats_free_on_craigslist_app', '0006_listing_hood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='price',
        ),
    ]
