# Generated by Django 5.2.1 on 2025-05-21 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='create_on',
            new_name='created_on',
        ),
    ]
