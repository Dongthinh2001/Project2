# Generated by Django 4.1.6 on 2023-03-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FootballPitch',
            fields=[
                ('id_pitch', models.AutoField(primary_key=True, serialize=False)),
                ('name_pitch', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('5', '5'), ('7', '7'), ('9', '9'), ('11', '11')], default='5', max_length=10)),
                ('time_slot', models.CharField(choices=[('T1', '8h-9h30'), ('T2', '9h30-11h'), ('T3', '13h-14h30'), ('T4', '14h30-16h'), ('T5', '16h-17h30'), ('T6', '17h30-19h'), ('T7', '19h-20h30'), ('T8', '20h30-22h')], default=None, max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('EM', 'Empty'), ('BO', 'Booked')], default='EM', max_length=50)),
            ],
        ),
    ]
