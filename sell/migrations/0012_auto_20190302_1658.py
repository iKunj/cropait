# Generated by Django 2.1.5 on 2019-03-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0011_buyer_demand_farmer_crops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer_demand',
            name='flag',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='farmer_crops',
            name='flag',
            field=models.IntegerField(default=0),
        ),
    ]
