# Generated by Django 3.2.7 on 2023-05-22 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attribution_preference', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribution_preference_course_preference',
            old_name='Attribution_preference',
            new_name='attribution_preference',
        ),
        migrations.RenameField(
            model_name='attribution_workload_supplementation',
            old_name='Attribution_preference',
            new_name='attribution_preference',
        ),
        migrations.RenameField(
            model_name='attribution_workload_supplementation',
            old_name='Workload_supplementation',
            new_name='workload_supplementation',
        ),
    ]