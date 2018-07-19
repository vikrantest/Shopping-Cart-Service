import datetime
from rest_framework import serializers
from orders.models import *

class CartProductSerializers(serializers.ModelSerializer):

	class Meta:
		model = CartProducts
		fields = ('id','product_id','product_price','product_quantity')


class CartSerializers(serializers.ModelSerializer):


	class Meta:
		model = Cart
		fields = ('cart_id','item_count','cart_price')






