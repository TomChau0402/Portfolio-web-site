# Generated by Django 5.2.1 on 2025-05-21 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_create_on_note_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='notes/'),
        ),
    ]
