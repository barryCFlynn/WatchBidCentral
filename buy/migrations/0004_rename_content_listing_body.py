# Generated by Django 4.2.10 on 2024-02-10 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='content',
            new_name='body',
        ),
    ]
