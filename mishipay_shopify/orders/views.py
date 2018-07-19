from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.orderservice import ShopifyProductHandlerService


class ProductListView(APIView):

	def get(self,request):
		product_servie_obj = ShopifyProductHandlerService()
		product_list = product_servie_obj('products_list')
		return Response(product_list,status=status.HTTP_200_OK)