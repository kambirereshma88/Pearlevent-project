# Generated by Django 5.0.1 on 2024-08-07 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_remove_event_oid_event_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
