# Generated by Django 4.2 on 2023-11-27 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0025_remove_education_candidate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='title',
            field=models.CharField(default='candidate', max_length=200, verbose_name='Title'),
        ),
    ]
