# Generated by Django 4.2 on 2023-12-08 19:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "candidate",
            "0033_rename_tag_stack_remove_project_tags_project_stack_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="achievements_en",
        ),
        migrations.RemoveField(
            model_name="project",
            name="achievements_ru",
        ),
    ]
