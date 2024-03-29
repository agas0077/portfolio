# Generated by Django 4.2 on 2023-11-24 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "candidate",
            "0014_remove_skill_tooltip_remove_skill_tooltip_en_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="skill",
            options={"ordering": ("-percent",)},
        ),
        migrations.AlterField(
            model_name="skill",
            name="percent",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="Percentage",
            ),
        ),
    ]
