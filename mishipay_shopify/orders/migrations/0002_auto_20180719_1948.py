# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-19 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOrderBaseData',
            fields=[
                ('commonbasedata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.CommonBaseData')),
                ('product_id', models.CharField(max_length=100)),
                ('variant_id', models.CharField(max_length=100)),
                ('product_quantity', models.IntegerField(default=1)),
                ('customer_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orders_details', to='orders.Orders')),
            ],
            options={
                'db_table': 'mishipay_order_data',
            },
            bases=('orders.commonbasedata',),
        ),
        migrations.RemoveField(
            model_name='commonbasedata',
            name='deleted_on',
        ),
        migrations.AddField(
            model_name='cartproducts',
            name='product_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cartproducts',
            name='product_quantity',
            field=models.IntegerField(default=1),
        ),
    ]
