# Generated by Django 4.2.2 on 2023-06-22 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empower', '0007_homepage_banner_homepage_bannercolor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.FloatField()),
                ('image', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]