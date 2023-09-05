# Generated by Django 4.1.7 on 2023-09-05 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attribution_preference', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribution_preference',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.job'),
        ),
        migrations.AddField(
            model_name='attribution_preference',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
