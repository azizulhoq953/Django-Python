# Generated by Django 4.2.4 on 2023-08-31 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phoneNumber',
            field=models.IntegerField(help_text='phone'),
        ),
    ]