# Generated by Django 2.2 on 2019-07-09 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_auto_20190709_0851'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Objective',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='objective_comments', to='jobs.Objective'),
        ),
    ]
