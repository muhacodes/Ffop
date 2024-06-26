# Generated by Django 5.0.3 on 2024-04-02 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Batch', '0002_batch_student'),
        ('Lesson', '0003_rename_department_id_lesson_department'),
        ('Student', '0003_student_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=255, unique=True)),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.CharField(blank=True, max_length=250, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='Pending', max_length=255)),
                ('invoice_date', models.DateField()),
                ('due_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='Batch.batch')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_invoices', to=settings.AUTH_USER_MODEL)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='Lesson.lesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='Student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Invoice.invoice')),
            ],
        ),
    ]
