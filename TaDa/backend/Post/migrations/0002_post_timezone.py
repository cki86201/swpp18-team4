# Generated by Django 2.1.2 on 2018-12-02 16:44

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timezone',
            field=django_mysql.models.ListCharField(models.CharField(max_length=30), max_length=620, null=True, size=20),
        ),
    ]
