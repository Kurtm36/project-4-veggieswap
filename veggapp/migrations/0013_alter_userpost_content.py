# Generated by Django 3.2.23 on 2024-01-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggapp', '0012_userpost_placeholder_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
