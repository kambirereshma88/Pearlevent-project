# Generated by Django 5.0.1 on 2024-07-30 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_customer_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Booking',
        ),
    ]
