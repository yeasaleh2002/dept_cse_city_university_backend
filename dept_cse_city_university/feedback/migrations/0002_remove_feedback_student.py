# Generated by Django 5.1.1 on 2024-11-20 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='student',
        ),
    ]
