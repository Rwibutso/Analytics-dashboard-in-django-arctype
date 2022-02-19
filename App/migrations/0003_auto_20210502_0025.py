# Generated by Django 3.1.7 on 2021-05-01 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20210428_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('username', models.TextField()),
                ('ip', models.CharField(max_length=40)),
                ('session', models.CharField(max_length=40)),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 5, 2, 0, 25, 40, 963981))),
            ],
        ),
        migrations.DeleteModel(
            name='LogoutRegister',
        ),
        migrations.DeleteModel(
            name='PageView',
        ),
    ]
