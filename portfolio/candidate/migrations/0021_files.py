# Generated by Django 4.2 on 2023-11-27 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0020_remove_softskill_level_remove_softskill_tooltip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='files/', verbose_name='File')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('change_date', models.DateTimeField(auto_now=True, verbose_name='Change date')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='candidate.candidate', verbose_name='Candidate')),
            ],
            options={
                'ordering': ('-change_date',),
            },
        ),
    ]
