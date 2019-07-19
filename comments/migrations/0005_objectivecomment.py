# Generated by Django 2.2 on 2019-07-09 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0023_auto_20190709_1404'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0004_auto_20190709_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectiveComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('objective', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='objective_comments', to='jobs.Objective')),
            ],
            options={
                'ordering': ('-comment_date',),
            },
        ),
    ]