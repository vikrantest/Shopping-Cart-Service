import os
import json
from rest_framework.decorators import  permission_classes
from rest_framework import permissions
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from products.productservice import *
from shopping_frontend.utils import BackendAPIUtils

# Create your views here.
token_file = os.getcwd()+"/shopping_frontend/token.json"

@permission_classes((permissions.AllowAny,))
class Signin(TemplateView):

	def get(self,request):
		return render(request, 'signin.html', {})

	def post(self,request):
		request_data = request.POST
		valid_login , token= BackendAPIUtils.signin(request_data)
		if not valid_login:
			return render(request, 'signin.html', {"error":"Invalid Credentials"})
		else:
			return HttpResponseRedirect("/webapp/products")

@permission_classes((permissions.AllowAny,))
class SignOut(TemplateView):


	def get(self,request):
		valid_logout= BackendAPIUtils.signout()
		if not valid_logout:
			return HttpResponseRedirect("/webapp/products")
		else:
			with open(token_file,"w") as token_obj:
				json.dump({}, token_obj)
			return HttpResponseRedirect("/webapp/signin")



@permission_classes((permissions.AllowAny,))
class ProductView(TemplateView):

	def __init__(self):
		self.product_service = ShopifyProductHandlerService()

	def get(self,request):
		products = self.product_service("products_list")
		# products = {"products":[{"id":1348337827942,"title":"Black Denim Jeans","body_html":"\u003cp\u003eBlue Denim Jeans Slim Fit\u003c\/p\u003e","vendor":"vikrant store test1","product_type":"Jeans","created_at":"2018-07-19T03:37:12-04:00","handle":"black-denim-jeans","updated_at":"2018-07-19T12:35:38-04:00","published_at":"2018-07-19T03:37:12-04:00","template_suffix":None,"tags":"mens t-shirt example","published_scope":"web","variants":[{"id":12381387456614,"product_id":1348337827942,"title":"Default Title","price":"11.00","sku":"30","position":1,"inventory_policy":"deny","compare_at_price":None,"fulfillment_service":"manual","inventory_management":"shopify","option1":"Default Title","option2":None,"option3":None,"created_at":"2018-07-19T03:37:12-04:00","updated_at":"2018-07-19T11:57:46-04:00","taxable":True,"barcode":None,"grams":53,"image_id":None,"inventory_quantity":20,"weight":0.053,"weight_unit":"kg","inventory_item_id":12629221474406,"old_inventory_quantity":20,"requires_shipping":True}],"options":[{"id":1819563786342,"product_id":1348337827942,"name":"Title","position":1,"values":["Default Title"]}],"images":[{"id":3655910031462,"product_id":1348337827942,"position":1,"created_at":"2018-07-19T12:35:38-04:00","updated_at":"2018-07-19T12:35:38-04:00","alt":None,"width":342,"height":400,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/bluedenim.jpg?v=1532018138","variant_ids":[]}],"image":{"id":3655910031462,"product_id":1348337827942,"position":1,"created_at":"2018-07-19T12:35:38-04:00","updated_at":"2018-07-19T12:35:38-04:00","alt":None,"width":342,"height":400,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/bluedenim.jpg?v=1532018138","variant_ids":[]}},{"id":1348337795174,"title":"Blue Denim Jeans","body_html":"\u003cp\u003eBlue Denim Jeans\u003c\/p\u003e","vendor":"vikrant store test1","product_type":"Jeans","created_at":"2018-07-19T03:37:12-04:00","handle":"blue-denim-jeans","updated_at":"2018-07-19T12:38:17-04:00","published_at":"2018-07-19T03:37:12-04:00","template_suffix":None,"tags":"mens t-shirt example","published_scope":"web","variants":[{"id":12381387423846,"product_id":1348337795174,"title":"Default Title","price":"6.00","sku":"30","position":1,"inventory_policy":"deny","compare_at_price":None,"fulfillment_service":"manual","inventory_management":"shopify","option1":"Default Title","option2":None,"option3":None,"created_at":"2018-07-19T03:37:12-04:00","updated_at":"2018-07-19T12:38:17-04:00","taxable":True,"barcode":"","grams":23,"image_id":None,"inventory_quantity":13,"weight":0.023,"weight_unit":"kg","inventory_item_id":12629221441638,"old_inventory_quantity":13,"requires_shipping":True}],"options":[{"id":1819563753574,"product_id":1348337795174,"name":"Title","position":1,"values":["Default Title"]}],"images":[{"id":3655919435878,"product_id":1348337795174,"position":1,"created_at":"2018-07-19T12:38:12-04:00","updated_at":"2018-07-19T12:38:12-04:00","alt":None,"width":342,"height":400,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/bluedenim_161d3881-34da-4f9a-b083-09232f1be288.jpg?v=1532018292","variant_ids":[]}],"image":{"id":3655919435878,"product_id":1348337795174,"position":1,"created_at":"2018-07-19T12:38:12-04:00","updated_at":"2018-07-19T12:38:12-04:00","alt":None,"width":342,"height":400,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/bluedenim_161d3881-34da-4f9a-b083-09232f1be288.jpg?v=1532018292","variant_ids":[]}},{"id":1348337860710,"title":"Brown Full Sleeves Hoodie","body_html":"\u003cp\u003eBrown Full Sleeves Hoodie\u003c\/p\u003e","vendor":"vikrant store test1","product_type":"T-Shirts","created_at":"2018-07-19T03:37:13-04:00","handle":"brown-full-sleeves-hoodie","updated_at":"2018-07-19T12:37:40-04:00","published_at":"2018-07-19T03:37:13-04:00","template_suffix":None,"tags":"mens t-shirt example","published_scope":"web","variants":[{"id":12381387489382,"product_id":1348337860710,"title":"Default Title","price":"12.00","sku":"30","position":1,"inventory_policy":"deny","compare_at_price":None,"fulfillment_service":"manual","inventory_management":"shopify","option1":"Default Title","option2":None,"option3":None,"created_at":"2018-07-19T03:37:13-04:00","updated_at":"2018-07-19T12:37:40-04:00","taxable":True,"barcode":"","grams":46,"image_id":None,"inventory_quantity":30,"weight":0.046,"weight_unit":"kg","inventory_item_id":12629221507174,"old_inventory_quantity":30,"requires_shipping":True}],"options":[{"id":1819563819110,"product_id":1348337860710,"name":"Title","position":1,"values":["Default Title"]}],"images":[{"id":3655915536486,"product_id":1348337860710,"position":1,"created_at":"2018-07-19T12:37:18-04:00","updated_at":"2018-07-19T12:37:30-04:00","alt":None,"width":558,"height":744,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/Zaful_Front_Pocket_Fleece_Hoodie_Brown_M_Cotton_Polyester_Spandex_Shirt_Length_Regular_Sleeves_Length_Full_IIFEPYE.jpg?v=1532018250","variant_ids":[]}],"image":{"id":3655915536486,"product_id":1348337860710,"position":1,"created_at":"2018-07-19T12:37:18-04:00","updated_at":"2018-07-19T12:37:30-04:00","alt":None,"width":558,"height":744,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/Zaful_Front_Pocket_Fleece_Hoodie_Brown_M_Cotton_Polyester_Spandex_Shirt_Length_Regular_Sleeves_Length_Full_IIFEPYE.jpg?v=1532018250","variant_ids":[]}},{"id":1348337926246,"title":"Dark Red Half Sleeve Shirt","body_html":"\u003cp\u003eGreen Polo T-shirt\u003c\/p\u003e","vendor":"vikrant store test1","product_type":"T-Shirts","created_at":"2018-07-19T03:37:13-04:00","handle":"dark-red-half-sleeve-shirt","updated_at":"2018-07-19T12:36:34-04:00","published_at":"2018-07-19T03:37:13-04:00","template_suffix":None,"tags":"mens t-shirt example","published_scope":"web","variants":[{"id":12381387554918,"product_id":1348337926246,"title":"Default Title","price":"7.00","sku":"30","position":1,"inventory_policy":"deny","compare_at_price":None,"fulfillment_service":"manual","inventory_management":"shopify","option1":"Default Title","option2":None,"option3":None,"created_at":"2018-07-19T03:37:13-04:00","updated_at":"2018-07-19T03:37:13-04:00","taxable":True,"barcode":None,"grams":23,"image_id":None,"inventory_quantity":10,"weight":0.023,"weight_unit":"kg","inventory_item_id":12629221572710,"old_inventory_quantity":10,"requires_shipping":True}],"options":[{"id":1819563884646,"product_id":1348337926246,"name":"Title","position":1,"values":["Default Title"]}],"images":[{"id":3655913308262,"product_id":1348337926246,"position":1,"created_at":"2018-07-19T12:36:34-04:00","updated_at":"2018-07-19T12:36:34-04:00","alt":None,"width":342,"height":445,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/dark_red.jpg?v=1532018194","variant_ids":[]}],"image":{"id":3655913308262,"product_id":1348337926246,"position":1,"created_at":"2018-07-19T12:36:34-04:00","updated_at":"2018-07-19T12:36:34-04:00","alt":None,"width":342,"height":445,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/dark_red.jpg?v=1532018194","variant_ids":[]}},{"id":1348297424998,"title":"Full Sleeve Red T-shirt","body_html":"Full Sleeve Red T-shirt with round neck.","vendor":"vikrant store test1","product_type":"","created_at":"2018-07-19T02:29:27-04:00","handle":"full-sleeve-red-t-shirt","updated_at":"2018-07-19T02:39:52-04:00","published_at":"2018-07-19T02:28:09-04:00","template_suffix":None,"tags":"","published_scope":"web","variants":[{"id":12381172629606,"product_id":1348297424998,"title":"Default Title","price":"500.00","sku":"30","position":1,"inventory_policy":"deny","compare_at_price":None,"fulfillment_service":"manual","inventory_management":"shopify","option1":"Default Title","option2":None,"option3":None,"created_at":"2018-07-19T02:29:27-04:00","updated_at":"2018-07-19T02:29:27-04:00","taxable":True,"barcode":"","grams":13,"image_id":None,"inventory_quantity":28,"weight":0.013,"weight_unit":"kg","inventory_item_id":12628972240998,"old_inventory_quantity":28,"requires_shipping":True}],"options":[{"id":1819512275046,"product_id":1348297424998,"name":"Title","position":1,"values":["Default Title"]}],"images":[{"id":3654219235430,"product_id":1348297424998,"position":1,"created_at":"2018-07-19T02:39:52-04:00","updated_at":"2018-07-19T02:39:52-04:00","alt":None,"width":900,"height":1200,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/no-logo-white-round-neck-full-sleeve-t-shirt.jpg?v=1531982392","variant_ids":[]}],"image":{"id":3654219235430,"product_id":1348297424998,"position":1,"created_at":"2018-07-19T02:39:52-04:00","updated_at":"2018-07-19T02:39:52-04:00","alt":None,"width":900,"height":1200,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/no-logo-white-round-neck-full-sleeve-t-shirt.jpg?v=1531982392","variant_ids":[]}},{"id":1348337762406,"title":"Full Sleeve White T-shirt","body_html":"\u003cp\u003eFull Sleeve Red T-shirt with round neck.\u003c\/p\u003e","vendor":"vikrant store test1","product_type":"T-Shirts","created_at":"2018-07-19T03:37:12-04:00","handle":"full-sleeve-white-t-shirt","updated_at":"2018-07-19T03:40:00-04:00","published_at":"2018-07-19T03:37:11-04:00","template_suffix":None,"tags":"mens t-shirt example","published_scope":"web","variants":[{"id":12381387161702,"product_id":1348337762406,"title":"Default Title","price":"5.00","sku":"30","position":1,"inventory_policy":"deny","compare_at_price":None,"fulfillment_service":"manual","inventory_management":"shopify","option1":"Default Title","option2":None,"option3":None,"created_at":"2018-07-19T03:37:12-04:00","updated_at":"2018-07-19T03:37:12-04:00","taxable":True,"barcode":None,"grams":13,"image_id":None,"inventory_quantity":28,"weight":0.013,"weight_unit":"kg","inventory_item_id":12629221212262,"old_inventory_quantity":28,"requires_shipping":True}],"options":[{"id":1819563688038,"product_id":1348337762406,"name":"Title","position":1,"values":["Default Title"]}],"images":[{"id":3654423871590,"product_id":1348337762406,"position":1,"created_at":"2018-07-19T03:37:12-04:00","updated_at":"2018-07-19T03:37:12-04:00","alt":None,"width":323,"height":434,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/shopify_shirt.png?v=1531985832","variant_ids":[]}],"image":{"id":3654423871590,"product_id":1348337762406,"position":1,"created_at":"2018-07-19T03:37:12-04:00","updated_at":"2018-07-19T03:37:12-04:00","alt":None,"width":323,"height":434,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/shopify_shirt.png?v=1531985832","variant_ids":[]}},{"id":1348337893478,"title":"Green Polo T-shirt","body_html":"\u003cp\u003eBrown Full Sleeves Hoodie\u003c\/p\u003e","vendor":"vikrant store test1","product_type":"T-Shirts","created_at":"2018-07-19T03:37:13-04:00","handle":"green-polo-tshirt","updated_at":"2018-07-19T12:36:27-04:00","published_at":"2018-07-19T03:37:13-04:00","template_suffix":None,"tags":"mens t-shirt example","published_scope":"web","variants":[{"id":12381387522150,"product_id":1348337893478,"title":"Default Title","price":"14.00","sku":"30","position":1,"inventory_policy":"deny","compare_at_price":None,"fulfillment_service":"manual","inventory_management":"shopify","option1":"Default Title","option2":None,"option3":None,"created_at":"2018-07-19T03:37:13-04:00","updated_at":"2018-07-19T03:37:13-04:00","taxable":True,"barcode":None,"grams":13,"image_id":None,"inventory_quantity":19,"weight":0.013,"weight_unit":"kg","inventory_item_id":12629221539942,"old_inventory_quantity":19,"requires_shipping":True}],"options":[{"id":1819563851878,"product_id":1348337893478,"name":"Title","position":1,"values":["Default Title"]}],"images":[{"id":3655913013350,"product_id":1348337893478,"position":1,"created_at":"2018-07-19T12:36:27-04:00","updated_at":"2018-07-19T12:36:27-04:00","alt":None,"width":900,"height":1200,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/red-tape-bottle-green-polo-t-shirt.jpg?v=1532018187","variant_ids":[]}],"image":{"id":3655913013350,"product_id":1348337893478,"position":1,"created_at":"2018-07-19T12:36:27-04:00","updated_at":"2018-07-19T12:36:27-04:00","alt":None,"width":900,"height":1200,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/red-tape-bottle-green-polo-t-shirt.jpg?v=1532018187","variant_ids":[]}},{"id":1348337959014,"title":"Packs Of 3 Socks","body_html":"\u003cp\u003eDark Red Half Sleeve Shirt\u003c\/p\u003e","vendor":"vikrant store test1","product_type":"Socks","created_at":"2018-07-19T03:37:14-04:00","handle":"pack-of-3-socks","updated_at":"2018-07-19T12:35:47-04:00","published_at":"2018-07-19T03:37:14-04:00","template_suffix":None,"tags":"mens t-shirt example","published_scope":"web","variants":[{"id":12381387587686,"product_id":1348337959014,"title":"Default Title","price":"50.00","sku":"30","position":1,"inventory_policy":"deny","compare_at_price":None,"fulfillment_service":"manual","inventory_management":"shopify","option1":"Default Title","option2":None,"option3":None,"created_at":"2018-07-19T03:37:14-04:00","updated_at":"2018-07-19T03:37:14-04:00","taxable":True,"barcode":None,"grams":21,"image_id":None,"inventory_quantity":28,"weight":0.021,"weight_unit":"kg","inventory_item_id":12629221605478,"old_inventory_quantity":28,"requires_shipping":True}],"options":[{"id":1819563917414,"product_id":1348337959014,"name":"Title","position":1,"values":["Default Title"]}],"images":[{"id":3655911047270,"product_id":1348337959014,"position":1,"created_at":"2018-07-19T12:35:47-04:00","updated_at":"2018-07-19T12:35:47-04:00","alt":None,"width":226,"height":223,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/socks.jpeg?v=1532018147","variant_ids":[]}],"image":{"id":3655911047270,"product_id":1348337959014,"position":1,"created_at":"2018-07-19T12:35:47-04:00","updated_at":"2018-07-19T12:35:47-04:00","alt":None,"width":226,"height":223,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/socks.jpeg?v=1532018147","variant_ids":[]}},{"id":1348337991782,"title":"Plain Black Shirt","body_html":"\u003cp\u003ePacks Of 3 Socks\u003c\/p\u003e","vendor":"vikrant store test1","product_type":"Shirts","created_at":"2018-07-19T03:37:14-04:00","handle":"plain-black-shirt","updated_at":"2018-07-19T12:36:14-04:00","published_at":"2018-07-19T03:37:14-04:00","template_suffix":None,"tags":"mens t-shirt example","published_scope":"web","variants":[{"id":12381387620454,"product_id":1348337991782,"title":"Default Title","price":"9.00","sku":"30","position":1,"inventory_policy":"deny","compare_at_price":None,"fulfillment_service":"manual","inventory_management":"shopify","option1":"Default Title","option2":None,"option3":None,"created_at":"2018-07-19T03:37:14-04:00","updated_at":"2018-07-19T03:37:14-04:00","taxable":True,"barcode":None,"grams":10,"image_id":None,"inventory_quantity":20,"weight":0.01,"weight_unit":"kg","inventory_item_id":12629221638246,"old_inventory_quantity":20,"requires_shipping":True}],"options":[{"id":1819563950182,"product_id":1348337991782,"name":"Title","position":1,"values":["Default Title"]}],"images":[{"id":3655912390758,"product_id":1348337991782,"position":1,"created_at":"2018-07-19T12:36:14-04:00","updated_at":"2018-07-19T12:36:14-04:00","alt":None,"width":225,"height":225,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/black_shirt.jpeg?v=1532018174","variant_ids":[]}],"image":{"id":3655912390758,"product_id":1348337991782,"position":1,"created_at":"2018-07-19T12:36:14-04:00","updated_at":"2018-07-19T12:36:14-04:00","alt":None,"width":225,"height":225,"src":"https:\/\/cdn.shopify.com\/s\/files\/1\/0014\/8989\/5526\/products\/black_shirt.jpeg?v=1532018174","variant_ids":[]}}]}
		cart = BackendAPIUtils.getCart()
		if cart.get("cart",None):
			item_count = cart["cart"].get("item_count",0)
		else:
			item_count = 0
		return render(request, 'products.html', {'products': products['products'],"cart_item_count":item_count})

@permission_classes((permissions.AllowAny,))
class CartView(TemplateView):

	def get(self,request):

		cart = BackendAPIUtils.getCart()

		return render(request, 'cart.html', {'cart': cart.get('cart',{})}) 

@permission_classes((permissions.AllowAny,))
class OrderView(TemplateView):

	def get(self,request):

		orders = BackendAPIUtils.getOrders()

		return render(request, 'orders.html', {'orders': orders})