# Generated by Django 3.0.5 on 2020-04-21 11:52

import azure.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('azure', '0004_auto_20200420_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predict',
            name='age',
            field=azure.models.IntegerRangeField(),
        ),
    ]
