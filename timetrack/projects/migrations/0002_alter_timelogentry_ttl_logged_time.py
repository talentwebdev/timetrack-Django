# Generated by Django 3.2.8 on 2021-10-07 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelogentry',
            name='ttl_logged_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
