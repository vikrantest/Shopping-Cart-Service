# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-19 11:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_cartproducts_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commonbasedata',
            name='deleted_on',
        ),
    ]
