# Generated by Django 5.0.6 on 2024-06-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flock_feed", "0002_alter_post_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
