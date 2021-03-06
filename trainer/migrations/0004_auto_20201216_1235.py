# Generated by Django 3.0.8 on 2020-12-16 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0064_auto_20201216_1235'),
        ('trainer', '0003_auto_20201202_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainercourse',
            name='coaching_courseid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.AlterField(
            model_name='trainercourse',
            name='countOfStudent',
            field=models.IntegerField(default=0),
        ),
    ]
