# Generated by Django 4.2 on 2023-04-28 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0005_remove_currencytype_currency_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='user', max_length=50),
        ),
    ]