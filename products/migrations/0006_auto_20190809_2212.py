# Generated by Django 2.2 on 2019-08-09 22:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190807_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmaproduct',
            name='licence_number',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(code='invalid_licence_number', message='No spaces allowed', regex='^[^\\s]+$')]),
        ),
    ]