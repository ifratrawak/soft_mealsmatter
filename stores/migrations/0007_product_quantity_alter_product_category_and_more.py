# Generated by Django 4.1.4 on 2023-10-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_product_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
