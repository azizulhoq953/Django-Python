# Generated by Django 4.2.4 on 2023-09-01 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_defaultd'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registration',
            new_name='authenticate',
        ),
        migrations.DeleteModel(
            name='cartdb',
        ),
        migrations.DeleteModel(
            name='Deleted',
        ),
    ]