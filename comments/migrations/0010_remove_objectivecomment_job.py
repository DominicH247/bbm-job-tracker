# Generated by Django 2.2 on 2019-07-09 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0009_objectivecomment_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectivecomment',
            name='job',
        ),
    ]