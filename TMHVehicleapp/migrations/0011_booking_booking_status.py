# Generated by Django 3.2 on 2021-12-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMHVehicleapp', '0010_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_status',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
