# Generated by Django 3.1.5 on 2021-01-08 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpage',
            name='session_name',
            field=models.CharField(default='', max_length=1000, unique=True),
        ),
    ]