# Generated by Django 4.2.4 on 2023-09-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_rename_registration_authenticate_delete_cartdb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticate',
            name='Password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]