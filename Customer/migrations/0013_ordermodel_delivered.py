# Generated by Django 4.0 on 2022-08-28 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0012_remove_ordermodel_delivered'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
