# Generated by Django 4.2 on 2023-11-27 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0015_alter_skill_options_alter_skill_percent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skill',
            new_name='HardSkill',
        ),
    ]
