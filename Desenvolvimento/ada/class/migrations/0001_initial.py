# Generated by Django 3.2.7 on 2023-05-22 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_class_id', models.CharField(max_length=20, verbose_name='registration class id')),
                ('period', models.CharField(choices=[('morning', 'morning'), ('afternoon', 'afternoon'), ('night', 'night')], max_length=45, verbose_name='period')),
                ('semester', models.IntegerField(verbose_name='semester')),
                ('is_high_school', models.BooleanField(default=True, verbose_name='is high school')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='area.area')),
            ],
        ),
    ]
