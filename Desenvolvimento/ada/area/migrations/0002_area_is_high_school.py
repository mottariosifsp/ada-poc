# Generated by Django 4.1.7 on 2023-05-24 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='is_high_school',
            field=models.BooleanField(default=True, verbose_name='is high school'),
        ),
    ]
