# Generated by Django 4.2 on 2023-11-27 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0022_rename_files_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='file',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='file',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='file',
            name='title_ru',
        ),
    ]
