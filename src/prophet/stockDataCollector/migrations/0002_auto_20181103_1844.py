# Generated by Django 2.1.3 on 2018-11-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockDataCollector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdata',
            name='date_trade',
            field=models.DateTimeField(),
        ),
    ]
