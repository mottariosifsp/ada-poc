# Generated by Django 4.1.7 on 2023-05-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_user_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='nome',
            field=models.CharField(max_length=14, null=True, verbose_name='nome'),
        ),
    ]