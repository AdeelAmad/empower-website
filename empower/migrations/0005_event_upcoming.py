# Generated by Django 4.2.2 on 2023-06-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empower', '0004_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='upcoming',
            field=models.BooleanField(default=False),
        ),
    ]
