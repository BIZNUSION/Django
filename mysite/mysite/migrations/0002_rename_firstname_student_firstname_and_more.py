# Generated by Django 5.0.4 on 2024-05-05 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='firstname',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='lastname',
            new_name='lastName',
        ),
    ]
