# Generated by Django 4.1.7 on 2023-09-04 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_alter_deadline_semester_alter_deadline_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadline',
            name='semester',
            field=models.IntegerField(verbose_name='semester'),
        ),
        migrations.AlterField(
            model_name='deadline',
            name='year',
            field=models.IntegerField(verbose_name='year'),
        ),
    ]
