# Generated by Django 4.1.7 on 2023-04-11 15:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("courses", "0004_rename_instructor_course_teacher"),
        ("attribution", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("professors", "0004_rename_professors_professor"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Professor",
            new_name="Professors",
        ),
    ]
