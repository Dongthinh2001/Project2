# Generated by Django 4.1.6 on 2023-03-14 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footballpitchs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footballpitch',
            name='status',
        ),
        migrations.RemoveField(
            model_name='footballpitch',
            name='time_slot',
        ),
    ]
