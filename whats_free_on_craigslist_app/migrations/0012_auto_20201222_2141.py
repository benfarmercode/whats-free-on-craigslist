# Generated by Django 3.1.3 on 2020-12-22 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whats_free_on_craigslist_app', '0011_auto_20201203_0146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'get_latest_by': ['creation_date'], 'ordering': ['creation_date'], 'verbose_name_plural': 'Searches'},
        ),
    ]