# Generated by Django 4.2.2 on 2023-06-08 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empower', '0005_event_upcoming'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('attribution', models.TextField()),
                ('width', models.IntegerField()),
            ],
        ),
    ]
