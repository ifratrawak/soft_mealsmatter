# Generated by Django 4.1.4 on 2023-11-08 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0009_alter_donation_donor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='donations.extendeduser'),
        ),
    ]
