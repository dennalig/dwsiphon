# Generated by Django 3.0.5 on 2021-01-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=10000, unique=True)),
                ('siphon_to_playlist', models.CharField(default='', max_length=1000, unique=True)),
                ('auto_siphon_weekly', models.BooleanField(default=False)),
                ('disconnect_account', models.BooleanField(default=False)),
            ],
        ),
    ]
