# Generated by Django 3.2.5 on 2021-07-17 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_weather'),
    ]

    operations = [
        migrations.DeleteModel(
            name='weather',
        ),
    ]