# Generated by Django 4.1.7 on 2023-09-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='name_job',
            field=models.CharField(choices=[('TWENTY_HOURS', 'TWENTY_HOURS'), ('FORTY_HOURS', 'FORTY_HOURS'), ('RDE', 'RDE'), ('TEMPORARY', 'TEMPORARY'), ('SUBSTITUTE', 'SUBSTITUTE')], max_length=45, verbose_name='name job'),
        ),
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, choices=[('TWENTY_HOURS', 'TWENTY_HOURS'), ('FORTY_HOURS', 'FORTY_HOURS'), ('RDE', 'RDE'), ('TEMPORARY', 'TEMPORARY'), ('SUBSTITUTE', 'SUBSTITUTE')], max_length=45, null=True, verbose_name='job'),
        ),
    ]
