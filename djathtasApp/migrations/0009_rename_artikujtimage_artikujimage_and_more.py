# Generated by Django 5.1.3 on 2024-12-05 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djathtasApp', '0008_artikujinfomues_alter_anetarsimi_gjinia_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArtikujtImage',
            new_name='ArtikujImage',
        ),
        migrations.RenameModel(
            old_name='ArtikujtVideo',
            new_name='ArtikujVideo',
        ),
    ]
