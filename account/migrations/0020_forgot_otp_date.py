# Generated by Django 3.0.8 on 2020-10-10 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_forgot_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='forgot_otp',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]
