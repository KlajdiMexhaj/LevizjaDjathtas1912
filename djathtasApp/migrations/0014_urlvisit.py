# Generated by Django 5.1.3 on 2025-01-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djathtasApp', '0013_delete_prova_alter_artikujinfomues_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, unique=True)),
                ('visit_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
