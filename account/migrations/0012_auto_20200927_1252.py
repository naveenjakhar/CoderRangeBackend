# Generated by Django 3.0.8 on 2020-09-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200927_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='kid_age',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='kid_age',
            field=models.CharField(max_length=15),
        ),
    ]
