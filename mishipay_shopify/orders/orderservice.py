import os
import sys
from common.utils import DatetimeUtil
from orders.models import *
from orders.serializers import CartSerializers ,CartProductSerializers
from products.productservice import ShopifyProductHandlerService

class ShopifyOrderHandlerService:


	def getOrdersList(self,param):
		print(Orders.objects.all())
		return True


class ShopifyCartHandlerService:


	def getOrCreatUserCart(self,user,serialized = True):
		try:
			cart , _ = Cart.objects.get_or_create(user_customer = user)
		except:
			cart = Cart.objects.create(user_customer = user)
		if serialized:
			cart_obj = CartSerializers(cart).data
			products = cart.get_products()
			if products:
				cart_products = CartProductSerializers(cart.get_products(),many=True).data
			else:
				cart_products = []
			cart_obj['products'] = cart_products

			return cart_obj
		else:
			return cart

	def AddProductToCart(self,user,product):
		error_message = "Some error ocurrered while adding this product to cart."
		if product.get('id',None):
			productservice = ShopifyProductHandlerService()
			res_data = productservice("product_details",product.get('id',None))
			if res_data.get('product',None):
				product_data = res_data['product']
				print(product_data)
				if product.get('quantity',0) > product_data['variants'][0].get('inventory_quantity',0):#expectd only one variant for a product
					return "Only "+str(product_data.get('inventory_quantity',0))+" left in stock"
				cart = self.getOrCreatUserCart(user,False)
				product['price'] = product_data['variants'][0]['price']
				cart.add_product(product)

				return "Product got successfully added in cart."
			else:
				return error_message
		else:
			return error_message

	def RemoveProductFromCart(self,user,p_id):
		if not p_id:
			return "Product not present in cart"
		cart = self.getOrCreatUserCart(user,False)
		cart.remove_product(p_id)
		return "Product successfully removed from cart"
