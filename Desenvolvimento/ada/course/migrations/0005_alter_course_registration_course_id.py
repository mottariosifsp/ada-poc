# Generated by Django 4.1.7 on 2023-05-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_course_id_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='registration_course_id',
            field=models.CharField(max_length=20, unique=True, verbose_name='registration course id'),
        ),
    ]
