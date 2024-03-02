# Generated by Django 4.0.6 on 2022-08-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srno', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('client', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('vlink', models.CharField(blank=True, max_length=200, null=True)),
                ('glink', models.CharField(blank=True, max_length=200, null=True)),
                ('pic', models.ImageField(blank=True, default='blank.png', null=True, upload_to='')),
            ],
        ),
    ]