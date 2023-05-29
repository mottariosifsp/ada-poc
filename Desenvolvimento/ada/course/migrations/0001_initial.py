# Generated by Django 4.1.7 on 2023-05-29 00:11

import common.validator.validator
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id_course', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('registration_course_id', models.CharField(max_length=20, unique=True, verbose_name='registration course id')),
                ('name_course', models.CharField(max_length=45, validators=[common.validator.validator.validate_uppercase], verbose_name='course name')),
                ('period', models.CharField(choices=[('morning', 'morning'), ('afternoon', 'afternoon'), ('night', 'night')], max_length=45, verbose_name='period')),
                ('hour_start', models.TimeField(verbose_name='start time')),
                ('hour_end', models.TimeField(verbose_name='end time')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='area.area')),
                ('block', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='area.block')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
            },
        ),
    ]
