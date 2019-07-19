# Generated by Django 2.2 on 2019-07-09 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_auto_20190707_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_status',
            field=models.CharField(blank=True, choices=[('Open', 'Open'), ('Closed', 'Closed')], default='', max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective_description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now=True, null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
                ('objective_status', models.CharField(blank=True, choices=[('To Start', 'To Start'), ('In Progress', 'In Progress'), ('Complete', 'Complete'), ('Obsolete', 'Obsolete')], default='', max_length=15, null=True)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.Job')),
            ],
        ),
    ]
