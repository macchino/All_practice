# Generated by Django 3.2 on 2021-11-17 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardmodel',
            old_name='titile',
            new_name='title',
        ),
    ]
