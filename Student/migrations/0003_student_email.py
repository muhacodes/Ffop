# Generated by Django 5.0.3 on 2024-04-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]