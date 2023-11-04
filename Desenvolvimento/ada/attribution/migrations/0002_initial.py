# Generated by Django 4.1.7 on 2023-11-03 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attribution', '0001_initial'),
        ('area', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherqueuepositionbackup',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teacherqueueposition',
            name='blockk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.blockk'),
        ),
        migrations.AddField(
            model_name='teacherqueueposition',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
