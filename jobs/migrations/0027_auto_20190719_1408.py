# Generated by Django 2.2 on 2019-07-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0026_auto_20190714_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]