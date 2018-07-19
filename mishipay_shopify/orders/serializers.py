import datetime
from rest_framework import serializers
from orders.models import *

class CartProductSerializers(serializers.ModelSerializer):

	class Meta:
		model = CartProducts
		fields = ('id','product_id','product_price','product_quantity','variant_id')

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






