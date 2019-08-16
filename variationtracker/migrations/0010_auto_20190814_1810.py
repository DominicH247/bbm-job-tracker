# Generated by Django 2.2 on 2019-08-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variationtracker', '0009_auto_20190814_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_outcome',
            field=models.CharField(blank=True, choices=[('Awaiting', 'Awaiting'), ('Approved', 'Approved'), ('RFI', 'RFI'), ('PVAR', 'PVAR'), ('Rejected', 'Rejected')], default='', max_length=10, null=True),
        ),
    ]
