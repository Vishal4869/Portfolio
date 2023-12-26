# Generated by Django 3.2.12 on 2022-07-15 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='application_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 16, 0, 2, 29, 929572)),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='invite',
            name='invite_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 16, 0, 2, 29, 930569)),
        ),
        migrations.AlterField(
            model_name='jobcreate',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 16, 0, 2, 29, 928572)),
        ),
    ]
