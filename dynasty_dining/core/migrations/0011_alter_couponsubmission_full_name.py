# Generated by Django 5.2 on 2025-04-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_couponsubmission_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponsubmission',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
    ]
