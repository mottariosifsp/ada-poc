# Generated by Django 4.1.7 on 2023-06-09 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blockk',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('registration_block_id', models.CharField(max_length=20, unique=True, verbose_name='registration block id')),
                ('name_block', models.CharField(max_length=90, unique=True, verbose_name='name block')),
                ('acronym', models.CharField(max_length=5, null=True, unique=True, verbose_name='acronym')),
            ],
            options={
                'verbose_name': 'blockk',
                'verbose_name_plural': 'blocks',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_area_id', models.CharField(max_length=20, unique=True, verbose_name='registration area id')),
                ('name_area', models.CharField(max_length=90, unique=True, verbose_name='name area')),
                ('acronym', models.CharField(max_length=5, null=True, unique=True, verbose_name='acronym')),
                ('exchange_area', models.BooleanField(default=True, verbose_name='exchange area')),
                ('is_high_school', models.BooleanField(default=True, verbose_name='is high school')),
                ('blocks', models.ManyToManyField(related_name='areas', to='area.blockk')),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
            },
        ),
    ]
