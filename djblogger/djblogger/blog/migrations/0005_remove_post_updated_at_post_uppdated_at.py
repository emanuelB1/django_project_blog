# Generated by Django 4.2.3 on 2023-07-20 02:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_remove_post_uppdated_at_post_updated_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="post",
            name="uppdated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
