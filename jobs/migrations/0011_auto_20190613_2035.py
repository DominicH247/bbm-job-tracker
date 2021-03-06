# Generated by Django 2.2 on 2019-06-13 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20190613_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.Job'),
        ),
    ]
