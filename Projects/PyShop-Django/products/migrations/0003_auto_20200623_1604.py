# Generated by Django 3.0.7 on 2020-06-23 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='offer',
            table='Offer',
        ),
        migrations.AlterModelTable(
            name='product',
            table='Products',
        ),
    ]