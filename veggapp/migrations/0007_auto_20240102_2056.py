# Generated by Django 3.2.23 on 2024-01-02 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('veggapp', '0006_auto_20240102_1926'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_item',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='catagory',
            field=models.IntegerField(choices=[(0, 'Fruit'), (1, 'Vegatable'), (2, 'Plant')], default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
