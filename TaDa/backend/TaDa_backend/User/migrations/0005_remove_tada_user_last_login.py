# Generated by Django 2.1.2 on 2018-11-20 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20181118_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tada_user',
            name='last_login',
        ),
    ]