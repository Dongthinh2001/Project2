# Generated by Django 4.1.6 on 2023-03-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time_slot',
            field=models.CharField(choices=[('T1', '8h-9h30'), ('T2', '9h30-11h'), ('T3', '13h-14h30'), ('T4', '14h30-16h'), ('T5', '16h-17h30'), ('T6', '17h30-19h'), ('T7', '19h-20h30'), ('T8', '20h30-22h')], default='T1', max_length=64),
        ),
    ]
