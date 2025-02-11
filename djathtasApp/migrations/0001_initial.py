# Generated by Django 5.1.3 on 2024-11-21 13:14

import django.utils.timezone
import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
    ]
