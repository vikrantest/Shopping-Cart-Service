import datetime
from rest_framework import serializers
from orders.models import *

class CartProductSerializers(serializers.ModelSerializer):

	class Meta:
		model = CartProducts
		fields = ('id','product_id','product_price','product_quantity','variant_id','product_title')

	def __init__(self, *args, **kwargs):
		fields = kwargs.pop('fields', None)
		super(CartProductSerializers, self).__init__(*args, **kwargs)
		if fields is not None:
			allowed = set(fields)
			existing = set(self.fields.keys())
			for field_name in existing - allowed:
				self.fields.pop(field_name)


class CartSerializers(serializers.ModelSerializer):


	class Meta:
		model = Cart
		fields = ('cart_id','item_count','cart_price')


class OrderSerializers(serializers.ModelSerializer):

	total_price = serializers.ReadOnlyField(source = "order_cart.cart_price")
	products = serializers.ReadOnlyField(source = "getProducts")


	class Meta:
		model = Orders
		fields = ('order_id','transaction_id','payment_method','order_status','total_price','products')





