# Generated by Django 2.1.3 on 2018-11-04 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockDataCollector', '0002_auto_20181103_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='companyNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol_trade', models.CharField(max_length=10)),
                ('company_name', models.CharField(max_length=100)),
            ],
        ),
    ]
