# Generated by Django 4.2.6 on 2023-10-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_remove_store_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='store_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/stores/'),
        ),
    ]
