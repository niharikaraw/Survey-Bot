# Generated by Django 4.0.4 on 2022-06-21 18:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 21, 18, 23, 18, 24217, tzinfo=utc), null=True),
        ),
    ]
