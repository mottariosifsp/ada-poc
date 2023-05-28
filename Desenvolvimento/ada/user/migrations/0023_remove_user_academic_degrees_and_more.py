# Generated by Django 4.2.1 on 2023-05-27 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_remove_history_academic_degrees_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='academic_degrees',
        ),
        migrations.AddField(
            model_name='history',
            name='academic_degrees',
            field=models.ManyToManyField(blank=True, to='user.academicdegree'),
        ),
    ]