# Generated by Django 5.2.3 on 2025-06-18 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labour',
            name='otp',
            field=models.CharField(default='112233', max_length=20),
        ),
    ]
