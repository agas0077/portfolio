# Generated by Django 4.2 on 2023-11-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0008_education_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='certificate/', verbose_name='Сертификат'),
        ),
    ]