# Generated by Django 3.2.5 on 2021-08-03 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SkillModel', '0012_construct_cutting_farming_husbandry_processing_social_userskill_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cutting',
            name='user',
        ),
        migrations.RemoveField(
            model_name='farming',
            name='user',
        ),
        migrations.RemoveField(
            model_name='husbandry',
            name='user',
        ),
        migrations.RemoveField(
            model_name='processing',
            name='user',
        ),
        migrations.RemoveField(
            model_name='social',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='construct',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='cutting',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='farming',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='husbandry',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='processing',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='social',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='vehicle',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='user',
        ),
        migrations.DeleteModel(
            name='construct',
        ),
        migrations.DeleteModel(
            name='cutting',
        ),
        migrations.DeleteModel(
            name='farming',
        ),
        migrations.DeleteModel(
            name='husbandry',
        ),
        migrations.DeleteModel(
            name='processing',
        ),
        migrations.DeleteModel(
            name='social',
        ),
        migrations.DeleteModel(
            name='UserSkill',
        ),
        migrations.DeleteModel(
            name='vehicle',
        ),
    ]