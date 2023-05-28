# Generated by Django 4.1.7 on 2023-05-28 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('area', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email address')),
                ('registration_id', models.CharField(max_length=9, unique=True, verbose_name='registration id')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('telephone', models.CharField(blank=True, max_length=10, null=True, verbose_name='telephone')),
                ('cell_phone', models.CharField(max_length=14, verbose_name='cell phone')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff status')),
                ('blocks', models.ManyToManyField(blank=True, to='area.block')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id_history', models.AutoField(primary_key=True, serialize=False)),
                ('birth', models.DateField(verbose_name='birth')),
                ('date_career', models.DateField(verbose_name='date career')),
                ('date_campus', models.DateField(verbose_name='date campus')),
                ('date_professor', models.DateField(verbose_name='date professor')),
                ('date_area', models.DateField(verbose_name='date area')),
                ('date_institute', models.DateField(verbose_name='date institute')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id_job', models.AutoField(primary_key=True, serialize=False)),
                ('name_job', models.CharField(max_length=255, verbose_name='name job')),
            ],
        ),
        migrations.CreateModel(
            name='Proficiency',
            fields=[
                ('id_proficiency', models.AutoField(primary_key=True, serialize=False)),
                ('is_competent', models.BooleanField(default=True, verbose_name='is competent')),
                ('course', models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.history'),
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.job'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
