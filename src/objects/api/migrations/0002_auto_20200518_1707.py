# Generated by Django 2.2.12 on 2020-05-18 15:07

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, help_text='Object data, based on OBJECTTYPE', verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='object',
            name='version',
            field=models.PositiveSmallIntegerField(help_text='Version of the OBJECTTYPE', verbose_name='version'),
        ),
    ]