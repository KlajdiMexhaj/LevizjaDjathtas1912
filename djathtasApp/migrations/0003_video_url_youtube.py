# Generated by Django 5.1.3 on 2024-11-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djathtasApp', '0002_remove_video_video_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url_youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]