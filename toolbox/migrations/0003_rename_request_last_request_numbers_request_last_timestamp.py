# Generated by Django 4.2.17 on 2024-12-16 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0002_numbers_request_last_request'),
    ]

    operations = [
        migrations.RenameField(
            model_name='numbers',
            old_name='request_last_request',
            new_name='request_last_timestamp',
        ),
    ]
