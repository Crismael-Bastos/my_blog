# Generated by Django 4.0.6 on 2022-08-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_post_image_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="new_image_post",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="post_img/%Y/%m/%d",
                verbose_name="Image",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="image_text",
            field=models.TextField(blank=True, null=True),
        ),
    ]
