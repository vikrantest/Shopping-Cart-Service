import os
import requests
import sys
import json
from requests.auth import HTTPBasicAuth
from django.conf import settings as my_settings


file_path = os.getcwd()+"/common/shopify_urls.json"

class ShopifyProductHandlerService:

	def __init__(self):
		self.URL_TOKEN = ["{APIKEY}","{PASSWORD}","{STOREURL}"]

	def __call__(self,arg,*args):
		if arg == "products_list":
			call_url = 'products_list'
			return self.getProductsList(call_url,None)
		elif arg == "product_details":
			call_url = 'product_details'
			return self.getProductsList(call_url,product = args[0])



	def getProductShopifyUrl(self,param,product):

		with open(file_path,'r') as fobj:
			data = json.load(fobj)
		
		url = data['products'][param]

		if product:
			return url.format(STOREURL=my_settings.STORE_URL,PRODUCT_ID=str(product))
		else:
			return url.format(STOREURL=my_settings.STORE_URL)


	def getProductsList(self,url_call,product=None):
		req_url = self.getProductShopifyUrl(url_call,product)
		data = requests.get(req_url,auth=HTTPBasicAuth(my_settings.SHOPIFY_API_KEY, my_settings.SHOPIFY_API_PASSWORD))

		if data.status_code == 200:
			return data.json()
		else:
			return {'products':[]}

