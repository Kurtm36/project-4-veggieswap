# Generated by Django 3.2.23 on 2024-01-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggapp', '0011_remove_userpost_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='placeholder_image',
            field=models.CharField(default=0, max_length=300),
        ),
    ]
