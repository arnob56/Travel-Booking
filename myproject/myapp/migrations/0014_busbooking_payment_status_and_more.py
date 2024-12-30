# Generated by Django 5.1.4 on 2024-12-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_busbooking_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='busbooking',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='busbooking',
            name='total_price',
            field=models.IntegerField(),
        ),
    ]
