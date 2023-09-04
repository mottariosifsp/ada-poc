# Generated by Django 4.1.7 on 2023-09-04 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherQueuePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherQueuePositionBackup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('blockk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.blockk')),
            ],
        ),
    ]
