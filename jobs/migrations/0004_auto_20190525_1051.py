# Generated by Django 2.2 on 2019-05-25 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0003_auto_20190525_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='personnel',
        ),
        migrations.AddField(
            model_name='job',
            name='personnel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addition_personnel', to=settings.AUTH_USER_MODEL),
        ),
    ]