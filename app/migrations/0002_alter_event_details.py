# Generated by Django 4.1.7 on 2024-11-19 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='details',
            field=models.TextField(max_length=10000),
        ),
    ]
