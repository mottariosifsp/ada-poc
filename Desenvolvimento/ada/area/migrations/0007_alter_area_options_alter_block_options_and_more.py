# Generated by Django 4.1.7 on 2023-05-28 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0006_merge_20230527_2216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': 'area', 'verbose_name_plural': 'areas'},
        ),
        migrations.AlterModelOptions(
            name='block',
            options={'verbose_name': 'block', 'verbose_name_plural': 'blocks'},
        ),
        migrations.AlterField(
            model_name='block',
            name='registration_block_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='registration block id'),
        ),
    ]
