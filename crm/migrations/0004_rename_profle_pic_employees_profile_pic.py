# Generated by Django 4.2.6 on 2023-11-09 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_rename_images_employees_profle_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='profle_pic',
            new_name='profile_pic',
        ),
    ]