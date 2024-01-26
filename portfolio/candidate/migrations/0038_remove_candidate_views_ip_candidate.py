# Generated by Django 4.2 on 2024-01-26 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0037_ip_alter_candidate_job_search_status_candidate_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='views',
        ),
        migrations.AddField(
            model_name='ip',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ips', to='candidate.candidate', verbose_name='Candidate'),
        ),
    ]
