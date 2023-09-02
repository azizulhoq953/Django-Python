# Generated by Django 4.2.4 on 2023-08-31 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_login_remove_registration_phonenumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]