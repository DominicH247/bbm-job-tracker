# Generated by Django 2.2 on 2019-07-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0018_auto_20190707_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='close_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
