# Generated by Django 5.0.7 on 2024-11-10 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_batch_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='credit',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
        ),
    ]
