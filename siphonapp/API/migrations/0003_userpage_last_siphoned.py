# Generated by Django 3.1.5 on 2021-01-09 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_userpage_session_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpage',
            name='last_siphoned',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 9, 17, 25, 41, 222743)),
        ),
    ]
