# Generated by Django 3.2.5 on 2021-08-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialModel', '0013_material_materialdetail_recipe_usermaterial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.JSONField()),
            ],
        ),
    ]
