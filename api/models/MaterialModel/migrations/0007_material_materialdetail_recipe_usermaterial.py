# Generated by Django 3.2.5 on 2021-08-07 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MaterialModel', '0006_auto_20210807_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='物资id')),
                ('name', models.CharField(max_length=20, verbose_name='物资名')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productivity', models.FloatField(verbose_name='物资自身产能')),
                ('level', models.SmallIntegerField(default=1, verbose_name='物资等级')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MaterialModel.material', verbose_name='物资')),
            ],
        ),
        migrations.CreateModel(
            name='UserMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(verbose_name='拥有数量')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MaterialModel.material', verbose_name='拥有物资')),
                ('material_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MaterialModel.materialdetail', verbose_name='物资等级')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('needed_count', models.FloatField(verbose_name='所需数量')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material', to='MaterialModel.material', verbose_name='物资')),
                ('material_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_detail', to='MaterialModel.materialdetail', verbose_name='物资等级')),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raw_material', to='MaterialModel.material', verbose_name='所需物资id')),
                ('raw_material_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raw_material_detail', to='MaterialModel.materialdetail', verbose_name='所需物资等级')),
            ],
        ),
    ]
