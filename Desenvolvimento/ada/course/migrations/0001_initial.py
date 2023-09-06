# Generated by Django 4.1.7 on 2023-09-06 03:57

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_course_id', models.CharField(max_length=20, unique=True, verbose_name='registration course id')),
                ('name_course', models.CharField(max_length=200, verbose_name='course name')),
                ('acronym', models.CharField(max_length=10, null=True, unique=True, verbose_name='acronym')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='area.area')),
                ('blockk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='area.blockk')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
            },
        ),
    ]
