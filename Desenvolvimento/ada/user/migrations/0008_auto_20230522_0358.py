# Generated by Django 3.2.7 on 2023-05-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20230522_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='id_history',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='id_job',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proficiency',
            name='id_proficiency',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
