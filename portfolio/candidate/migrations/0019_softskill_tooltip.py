# Generated by Django 4.2 on 2023-11-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0018_softskill_title_en_softskill_title_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='softskill',
            name='tooltip',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Tooltip'),
        ),
    ]
