# Generated by Django 5.0.1 on 2024-07-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_remove_event_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='bookedby',
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
