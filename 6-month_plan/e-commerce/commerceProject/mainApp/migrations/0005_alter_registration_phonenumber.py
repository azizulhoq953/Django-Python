# Generated by Django 4.2.4 on 2023-08-31 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_alter_registration_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phoneNumber',
            field=models.IntegerField(),
        ),
    ]
