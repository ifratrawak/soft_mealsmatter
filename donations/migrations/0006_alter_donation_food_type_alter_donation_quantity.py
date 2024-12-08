# Generated by Django 4.2.6 on 2023-10-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_alter_donation_donor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='food_type',
            field=models.CharField(default='Edible', max_length=100),
        ),
        migrations.AlterField(
            model_name='donation',
            name='quantity',
            field=models.CharField(default='1 kg', max_length=100),
        ),
    ]
