# Generated by Django 4.2 on 2023-04-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0009_paymentrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrequest',
            name='isAccepted',
            field=models.BooleanField(default=False),
        ),
    ]
