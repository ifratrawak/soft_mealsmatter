# Generated by Django 4.2.6 on 2023-10-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0006_alter_donation_food_type_alter_donation_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='expiry_date',
            field=models.DateField(default='2025-10-10'),
        ),
    ]
