# Generated by Django 5.1.3 on 2024-11-25 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djathtasApp', '0003_video_url_youtube'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.RemoveField(
            model_name='video',
            name='url_youtube',
        ),
    ]
