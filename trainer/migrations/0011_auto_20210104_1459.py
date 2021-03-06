# Generated by Django 3.0.8 on 2021-01-04 09:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0071_auto_20210104_1459'),
        ('trainer', '0010_auto_20201230_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 1, 4, 9, 29, 22, 475446, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trainercourse',
            name='coaching_courseid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Courses'),
        ),
        migrations.CreateModel(
            name='Class_Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('textReview', models.TextField()),
                ('classid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.Trainercourse')),
            ],
        ),
    ]
