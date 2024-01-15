# Generated by Django 3.2.23 on 2024-01-15 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('veggapp', '0013_alter_userpost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='content',
            field=models.Field(blank=True),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='placeholder_image',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
