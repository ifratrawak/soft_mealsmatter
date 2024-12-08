# Generated by Django 4.2.6 on 2023-10-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0007_alter_donation_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='location',
            field=models.CharField(choices=[('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Mohammadpur', 'Mohammadpur'), ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'), ('Mirpur', 'Mirpur'), ('Shamoli', 'Shamoli'), ('Adabor', 'Adabor'), ('Green Road', 'Green Road'), ('Uttara', 'Uttara'), ('Azimpur', 'Azimpur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'), ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'), ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh')], max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='photo',
            field=models.ImageField(default=None, upload_to='images/users'),
        ),
    ]
