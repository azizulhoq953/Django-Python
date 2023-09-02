# Generated by Django 4.2.4 on 2023-08-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps1', '0006_alter_login_managers_remove_login_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='password',
        ),
        migrations.AddField(
            model_name='login',
            name='email',
            field=models.EmailField(default='SOME STRING', max_length=33),
        ),
        migrations.AddField(
            model_name='login',
            name='username',
            field=models.CharField(default='SOME STRING', max_length=55),
        ),
        migrations.AlterField(
            model_name='login',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
