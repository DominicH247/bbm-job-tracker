# Generated by Django 2.2 on 2019-07-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_auto_20190707_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='close_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
