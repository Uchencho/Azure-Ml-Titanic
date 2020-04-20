# Generated by Django 3.0.5 on 2020-04-20 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predict',
            name='parents',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=3),
        ),
        migrations.AlterField(
            model_name='predict',
            name='siblings',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=3),
        ),
    ]
