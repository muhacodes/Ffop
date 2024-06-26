# Generated by Django 5.0.3 on 2024-04-03 10:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Batch', '0002_batch_student'),
        ('Invoice', '0002_remove_invoice_payment_method_and_more'),
        ('Lesson', '0003_rename_department_id_lesson_department'),
        ('Student', '0003_student_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Batch.batch'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson.lesson'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.student'),
        ),
    ]
