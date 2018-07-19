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

	def __call__(self,arg):
		if arg == "products_list":
			return self.getProductsList()

	def getShopifyUrl(self,param):

		with open(file_path,'r') as fobj:
			data = json.load(fobj)
		
		url = data['products'][param]

		return url.format(STOREURL=my_settings.STORE_URL)


	def getProductsList(self):
		req_url = self.getShopifyUrl('products_list')
		print(req_url)

		data = requests.get(req_url,auth=HTTPBasicAuth(my_settings.SHOPIFY_API_KEY, my_settings.SHOPIFY_API_PASSWORD))
		print(dir(data),data.status_code)
		if data.status_code == 200:
			return data.json()
		else:
			return {'products':[]}

