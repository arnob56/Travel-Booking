# Generated by Django 5.1.4 on 2024-12-29 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_train_trainbooking_rename_bus_busbooking_bus_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('car_serial', models.CharField(max_length=255)),
                ('car_name', models.CharField(max_length=255)),
                ('departure_location', models.CharField(max_length=255)),
                ('destination_location', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('journey_date', models.DateField()),
                ('fare', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=255)),
                ('event_location', models.CharField(max_length=255)),
                ('event_date', models.DateField()),
                ('event_type', models.CharField(choices=[('BPL', 'BPL'), ('Movie', 'Movie')], max_length=10)),
                ('total_seats', models.IntegerField()),
                ('available_seats', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotel_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=255)),
                ('hotel_location', models.CharField(max_length=255)),
                ('journey_date', models.DateField()),
                ('total_rooms', models.IntegerField()),
                ('available_rooms', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Launch',
            fields=[
                ('launch_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('launch_name', models.CharField(max_length=255)),
                ('departure_location', models.CharField(max_length=255)),
                ('destination_location', models.CharField(max_length=255)),
                ('start_time', models.TimeField()),
                ('arival_time', models.TimeField()),
                ('journey_date', models.DateField()),
                ('total_seats', models.IntegerField()),
                ('available_seats', models.IntegerField()),
                ('fare', models.IntegerField()),
            ],
        ),
    ]