# Generated by Django 3.1.7 on 2021-05-02 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20210502_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditProfileEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 5, 2, 16, 49, 13, 594642))),
            ],
        ),
        migrations.CreateModel(
            name='LoginEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 5, 2, 16, 49, 13, 594642))),
            ],
        ),
        migrations.CreateModel(
            name='LogoutEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 5, 2, 16, 49, 13, 595623))),
            ],
        ),
        migrations.CreateModel(
            name='RegisterEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 5, 2, 16, 49, 13, 593649))),
            ],
        ),
        migrations.CreateModel(
            name='ViewPageEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=40)),
                ('session', models.CharField(max_length=40)),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 5, 2, 16, 49, 13, 594642))),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 16, 49, 13, 593649)),
        ),
    ]