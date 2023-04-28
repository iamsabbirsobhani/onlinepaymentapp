# Generated by Django 4.2 on 2023-04-27 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0002_currencytype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currencytype',
            name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='currency_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='payapp.currencytype'),
        ),
    ]
