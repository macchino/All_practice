# Generated by Django 3.2 on 2021-11-15 03:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='duedate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('bt1', 'high'), ('bt2', 'normal'), ('bt3', 'usual')], default='bt1', max_length=50),
            preserve_default=False,
        ),
    ]
