# Generated by Django 4.1.7 on 2023-05-26 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, verbose_name='name')),
                ('deadline_start', models.DateTimeField(verbose_name='deadline start')),
                ('deadline_end', models.DateTimeField(verbose_name='deadline end')),
            ],
        ),
    ]
