# Generated by Django 4.2 on 2023-04-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='1', upload_to='previews/', verbose_name='Превью'),
            preserve_default=False,
        ),
    ]