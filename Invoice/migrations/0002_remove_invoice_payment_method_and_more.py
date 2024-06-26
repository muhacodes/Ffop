# Generated by Django 5.0.3 on 2024-04-02 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='transaction_id',
        ),
        migrations.AddField(
            model_name='payment',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
