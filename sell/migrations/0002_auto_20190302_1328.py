# Generated by Django 2.1.5 on 2019-03-02 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='buyer_demand',
        ),
        migrations.DeleteModel(
            name='farmer_crops',
        ),
    ]
