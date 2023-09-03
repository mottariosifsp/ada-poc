# Generated by Django 4.1.7 on 2023-09-03 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_criteria', models.CharField(max_length=90, verbose_name='name criteria')),
                ('number_criteria', models.IntegerField(null=True, unique=True, verbose_name='number criteria')),
                ('is_select', models.BooleanField(default=False, verbose_name='is selected')),
            ],
        ),
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, verbose_name='name')),
                ('deadline_start', models.DateTimeField(verbose_name='deadline start')),
                ('deadline_end', models.DateTimeField(verbose_name='deadline end')),
                ('semester', models.CharField(max_length=1, verbose_name='semester')),
                ('blockk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='area.blockk')),
            ],
            options={
                'verbose_name': 'deadline',
                'verbose_name_plural': 'deadlines',
            },
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_alert', models.CharField(max_length=90, verbose_name='name alert')),
                ('title', models.CharField(blank=True, max_length=45, null=True, verbose_name='title')),
                ('description', models.TextField(max_length=500, verbose_name='description')),
                ('blockk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='area.blockk')),
            ],
            options={
                'verbose_name': 'alert',
                'verbose_name_plural': 'alerts',
            },
        ),
    ]
