# Generated by Django 3.2 on 2021-12-29 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TMHVehicleapp', '0008_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]