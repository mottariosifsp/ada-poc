# Generated by Django 4.1.7 on 2023-06-09 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribution_preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'attribution_preference',
                'verbose_name_plural': 'attribution_preferences',
            },
        ),
        migrations.CreateModel(
            name='Attribution_preference_course_preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'attribution_preference_course_preference',
                'verbose_name_plural': 'attribution_preference_course_preferences',
            },
        ),
        migrations.CreateModel(
            name='Course_preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_course', models.IntegerField(verbose_name='count course')),
                ('priority', models.CharField(choices=[('primary', 'PRIMARY'), ('secondary', 'SECONDARY')], max_length=45, verbose_name='priority')),
                ('period', models.CharField(choices=[('morning', 'MORNING'), ('afternoon', 'AFTERNOON'), ('night', 'NIGHT')], max_length=45, verbose_name='period')),
            ],
            options={
                'verbose_name': 'course_preference',
                'verbose_name_plural': 'course_preferences',
            },
        ),
        migrations.CreateModel(
            name='Preference_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'MONDAY'), ('tuesday', 'TUESDAY'), ('wednesday', 'WEDNESDAY'), ('thursday', 'THURSDAY'), ('friday', 'FRIDAY'), ('saturday', 'SATURDAY')], max_length=45, verbose_name='day')),
                ('attribution_preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribution_preference.attribution_preference')),
            ],
            options={
                'verbose_name': 'preference_schedule',
                'verbose_name_plural': 'preference_schedules',
            },
        ),
    ]
