# Generated by Django 5.1.4 on 2024-12-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_busbooking_bus_name_remove_busbooking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='busbooking',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]