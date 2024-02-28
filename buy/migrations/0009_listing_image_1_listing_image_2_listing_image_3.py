# Generated by Django 4.2.10 on 2024-02-26 15:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0008_alter_comment_author_alter_comment_parent_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image_1',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image_1'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_2',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image_2'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_3',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image_3'),
        ),
    ]