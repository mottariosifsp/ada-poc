# Generated by Django 3.2.7 on 2023-05-22 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timetable', '0002_timetable_user'),
        ('course', '0002_auto_20230522_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribution_preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teaching_support_activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='name')),
                ('duration', models.TimeField(verbose_name='duration')),
            ],
        ),
        migrations.CreateModel(
            name='Workload_supplementation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='name')),
                ('duration', models.TimeField(verbose_name='duration')),
            ],
        ),
        migrations.CreateModel(
            name='Teaching_support_activity_attribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribution_preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribution_preference.attribution_preference')),
            ],
        ),
        migrations.CreateModel(
            name='Preference_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday')], max_length=45, verbose_name='day')),
                ('attribution_preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribution_preference.attribution_preference')),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.timeslot')),
            ],
        ),
        migrations.CreateModel(
            name='course_preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_course', models.IntegerField(verbose_name='count course')),
                ('priority', models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary')], max_length=45, verbose_name='day')),
                ('period', models.CharField(choices=[('morning', 'morning'), ('afternoon', 'afternoon'), ('night', 'night')], max_length=45, verbose_name='period')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Attribution_workload_supplementation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attribution_preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribution_preference.attribution_preference')),
                ('Workload_supplementation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribution_preference.workload_supplementation')),
            ],
        ),
        migrations.CreateModel(
            name='Attribution_preference_course_preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attribution_preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribution_preference.attribution_preference')),
                ('course_preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribution_preference.course_preference')),
            ],
        ),
    ]
