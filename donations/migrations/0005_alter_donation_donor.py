# Generated by Django 4.2.6 on 2023-10-14 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_alter_donation_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='donations.extendeduser'),
        ),
    ]
