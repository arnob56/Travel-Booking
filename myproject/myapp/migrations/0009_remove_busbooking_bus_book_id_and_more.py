# Generated by Django 5.1.4 on 2024-12-29 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_air_alter_busbooking_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busbooking',
            name='bus_book_id',
        ),
        migrations.RemoveField(
            model_name='busbooking',
            name='total_price',
        ),
        migrations.AddField(
            model_name='busbooking',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1001, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='busbooking',
            name='passenger_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='busbooking',
            name='passenger_phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='busbooking',
            name='selected_seats',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='AirBooking',
            fields=[
                ('plane_book_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('passenger_name', models.CharField(max_length=255)),
                ('passenger_phone', models.CharField(max_length=14)),
                ('selected_seats', models.CharField(max_length=200)),
                ('total_price', models.IntegerField(default=0)),
                ('air', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.air')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
