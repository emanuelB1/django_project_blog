# Generated by Django 4.2.3 on 2023-07-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_alter_post_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image_webp",
            field=models.ImageField(
                blank=True, null=True, upload_to="post_images_webp"
            ),
        ),
    ]
