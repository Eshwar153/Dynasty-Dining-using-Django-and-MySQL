# Generated by Django 5.2 on 2025-04-09 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_booking_special_requests_booking_guests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='number_of_people',
        ),
    ]
