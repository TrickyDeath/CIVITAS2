# Generated by Django 3.2.4 on 2021-09-18 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RecipesModel', '0006_auto_20210918_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input_Recipe_Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='数量')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RecipesModel.raw_materialdetail', verbose_name='输入物资')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RecipesModel.recipes', verbose_name='配方id')),
            ],
            options={
                'verbose_name_plural': '所需食材表',
            },
        ),
    ]
