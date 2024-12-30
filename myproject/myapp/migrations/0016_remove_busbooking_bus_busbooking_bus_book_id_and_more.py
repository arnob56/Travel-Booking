# Generated by Django 5.1.4 on 2024-12-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_busbooking_bus_alter_busbooking_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busbooking',
            name='bus',
        ),
        migrations.AddField(
            model_name='busbooking',
            name='bus_book_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='busbooking',
            name='total_price',
            field=models.IntegerField(),
        ),
    ]