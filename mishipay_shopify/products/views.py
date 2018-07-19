from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.decorators import  permission_classes
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.productservice import ShopifyProductHandlerService

@permission_classes((permissions.AllowAny,))
class ProductListView(APIView):

	def get(self,request):
		product_servie_obj = ShopifyProductHandlerService()
		product_list = product_servie_obj('products_list')
		return Response(product_list,status=status.HTTP_200_OK)