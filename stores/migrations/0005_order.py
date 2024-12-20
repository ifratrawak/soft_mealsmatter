# Generated by Django 4.1.4 on 2023-10-25 19:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_category_customer_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.product')),
            ],
        ),
    ]
