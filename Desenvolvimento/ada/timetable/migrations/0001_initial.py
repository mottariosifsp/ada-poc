# Generated by Django 4.1.7 on 2023-11-08 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day_combo',
            fields=[
                ('day_combo_id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(choices=[('monday', 'MONDAY'), ('tuesday', 'TUESDAY'), ('wednesday', 'WEDNESDAY'), ('thursday', 'THURSDAY'), ('friday', 'FRIDAY'), ('saturday', 'SATURDAY')], max_length=45, verbose_name='day')),
            ],
            options={
                'verbose_name': 'day_combo',
                'verbose_name_plural': 'day_combos',
            },
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, null=True, verbose_name='position')),
                ('hour_start', models.TimeField(verbose_name='hour start')),
                ('hour_end', models.TimeField(verbose_name='hour end')),
            ],
            options={
                'verbose_name': 'timeslot',
                'verbose_name_plural': 'timeslots',
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'timetable',
                'verbose_name_plural': 'timetables',
            },
        ),
        migrations.CreateModel(
            name='Timetable_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=45, null=True, verbose_name='year')),
                ('timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable_user', to='timetable.timetable')),
            ],
            options={
                'verbose_name': 'timetable_user',
                'verbose_name_plural': 'timetable_users',
            },
        ),
    ]
