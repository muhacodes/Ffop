# Generated by Django 5.0.3 on 2024-03-28 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lesson', '0002_rename_department_lesson_department_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='department_id',
            new_name='department',
        ),
    ]
