import os
import sys
import json
import requests
from django.conf import settings as my_settings
from requests.auth import HTTPBasicAuth
from common.utils import DatetimeUtil
from orders.models import *
from orders.serializers import CartSerializers ,CartProductSerializers
from products.productservice import ShopifyProductHandlerService

file_path = os.getcwd()+"/common/shopify_urls.json"

class ShopifyOrderHandlerService:


	def getOrdersList(self,param):
		return Orders.objects.filter(order_cart__user_customer = param)

	def getOrderShopifyUrl(self,param):

		with open(file_path,'r') as fobj:
			data = json.load(fobj)
		
		url = data['orders'][param]

		return url.format(STOREURL=my_settings.STORE_URL)


	def checkoutOrder(self,user):
		cart = ShopifyCartHandlerService().getOrCreatUserCart(user,False)
		order = Orders(order_cart = cart,order_completion_time = DatetimeUtil.unixtime())
		order.order_status = 'completed'
		if self.updateShopifyCart(cart):
			order.save()
			order.setOrderMetaData()
			cart.status = 'inactive'
			return True
		return False

	def getSopifyOrderPayload(self,cart):
		# line_items_data = CartProductSerializers(cart.get_products(),many=True,fields=["product_quantity","variant_id"]).data
		line_items_data = CartProductSerializers(cart.getProducts(),many=True).data
		line_items = []
		for data in line_items_data:
			line_items.append({"variant_id":int(data["variant_id"]),"quantity":data['product_quantity']})
		base_payload = {
			  "order": {
			    "line_items": line_items,
			    "inventory_behaviour": "decrement_obeying_policy"
			  }
			}

		return base_payload

	def updateShopifyCart(self,cart):
		req_url = self.getOrderShopifyUrl("create_order")
		payload = self.getSopifyOrderPayload(cart)
		headers = {'content-type': 'application/json'}
		data = requests.post(req_url,data=json.dumps(payload), headers=headers,auth=HTTPBasicAuth(my_settings.SHOPIFY_API_KEY, my_settings.SHOPIFY_API_PASSWORD))
		if data.status_code == 201:
			return True
		else:
			return False




class ShopifyCartHandlerService:


	def getOrCreatUserCart(self,user,serialized = True):
		try:
			cart , _ = Cart.objects.get_or_create(user_customer = user,status = 'active')
		except:
			cart = Cart.objects.create(user_customer = user,status = 'active')
		if serialized:
			cart_obj = CartSerializers(cart).data
			products = cart.getProducts()
			if products:
				cart_products = CartProductSerializers(products,many=True).data
			else:
				cart_products = []
			cart_obj['products'] = cart_products

			return cart_obj
		else:
			return cart

	def AddProductToCart(self,user,product):
		error_message = "Some error ocurrered while adding this product to cart."
		if all([product.get('product_id',None) , product.get('variant_id',None)]) :
			productservice = ShopifyProductHandlerService()
			res_data = productservice("product_details",product.get('product_id',None))
			if res_data.get('product',None):
				product_data = res_data['product']
				valid_variant = False
				for data in product_data['variants']:
					if int(data['id']) == int(product.get('variant_id')):
						valid_variant = True
						break
				if not valid_variant:
					return "Invalid Variant id." , True

				if int(product.get('quantity',0)) > int(product_data['variants'][0].get('inventory_quantity',0)):#expectd only one variant for a product
					return "Only "+str(product_data['variants'][0].get('inventory_quantity',0))+" left in stock", True
				cart = self.getOrCreatUserCart(user,False)
				product['price'] = product_data['variants'][0]['price']
				product['title'] = product_data['title']
				cart.addProduct(product)

				return "Product got successfully added in cart." , False
			else:
				return error_message , True
		else:
			return error_message, True

	def RemoveProductFromCart(self,user,p_id):
		if not p_id:
			return "Product not present in cart" , True
		cart = self.getOrCreatUserCart(user,False)
		if cart.removeProduct(p_id):
			return "Product successfully removed from cart" , False
		else:
			return "Some error occured while removing item from cart" , True
