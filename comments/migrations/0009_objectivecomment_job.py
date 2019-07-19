# Generated by Django 2.2 on 2019-07-09 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0023_auto_20190709_1404'),
        ('comments', '0008_objectivecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectivecomment',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_objective_comments', to='jobs.Job'),
        ),
    ]