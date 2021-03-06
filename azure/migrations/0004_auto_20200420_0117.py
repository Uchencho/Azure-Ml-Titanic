# Generated by Django 3.0.5 on 2020-04-20 01:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azure', '0003_auto_20200420_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predict',
            name='age',
            field=models.IntegerField(default=25, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='predict',
            name='parents',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='predict',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', max_length=10),
        ),
        migrations.AlterField(
            model_name='predict',
            name='siblings',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='predict',
            name='ticket_class',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=0),
        ),
    ]
