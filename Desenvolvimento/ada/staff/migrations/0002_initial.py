<<<<<<< HEAD
# Generated by Django 4.1.7 on 2023-11-02 00:24
=======
# Generated by Django 4.1.7 on 2023-11-03 20:04
>>>>>>> 53be2f9e1a979e486cab79cf2e26ce32a738464b

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
