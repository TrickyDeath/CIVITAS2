# Generated by Django 3.2.5 on 2021-08-07 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialModel', '0004_auto_20210807_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialdetail',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MaterialModel.material', verbose_name='物资'),
        ),
    ]
