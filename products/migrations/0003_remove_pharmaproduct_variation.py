# Generated by Django 2.2 on 2019-08-07 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_pharmaproduct_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmaproduct',
            name='variation',
        ),
    ]
