# Generated by Django 3.1.7 on 2021-04-28 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoutRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 4, 28, 17, 21, 58, 418012))),
            ],
        ),
        migrations.AlterField(
            model_name='pageview',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 17, 21, 58, 418012)),
        ),
    ]
