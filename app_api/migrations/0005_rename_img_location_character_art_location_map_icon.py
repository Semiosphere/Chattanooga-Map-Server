# Generated by Django 4.0.4 on 2022-06-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0004_location_discovered_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='img',
            new_name='character_art',
        ),
        migrations.AddField(
            model_name='location',
            name='map_icon',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]