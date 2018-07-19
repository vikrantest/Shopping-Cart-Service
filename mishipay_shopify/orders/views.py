from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.decorators import  permission_classes
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.orderservice import ShopifyOrderHandlerService , ShopifyCartHandlerService

@permission_classes((permissions.IsAuthenticated,))
class OrderView(APIView):

	def __init__(self):
		self.order_service_obj = ShopifyOrderHandlerService()

	def get(self,request):
		order_list = self.order_service_obj.getOrdersList(request.user)
		return Response({},status=status.HTTP_200_OK)





@permission_classes((permissions.IsAuthenticated,))
class CartView(APIView):

	def __init__(self):
		self.cart_service_obj = ShopifyCartHandlerService()

	def get(self,request):
		requst_data = request.data
		cart = self.cart_service_obj.getOrCreatUserCart(request.user)
		return Response({'cart':cart},status=status.HTTP_200_OK)

	def put(self,request):
		requst_data = request.data
		cart,error = self.cart_service_obj.AddProductToCart(request.user,requst_data.get('product',{}))
		if error:
			status_code = status.HTTP_400_BAD_REQUEST
		else:
			status_code = status.HTTP_200_OK
		return Response({'message':cart},status=status.HTTP_200_OK)


	def delete(self,request):
		requst_data = request.data
		cart , error = self.cart_service_obj.RemoveProductFromCart(request.user,requst_data.get('cart_product_id',{}))
		if error:
			status_code = status.HTTP_400_BAD_REQUEST
		else:
			status_code = status.HTTP_200_OK
		return Response({'message':cart},status=status_code)

@permission_classes((permissions.IsAuthenticated,))
class CartCheckoutView(APIView):

	def __init__(self):
		self.order_service_obj = ShopifyOrderHandlerService()

	def post(self,request):
		if self.order_service_obj.checkoutOrder(request.user):
			return Response({'message':"Order successfully placed."},status=status.HTTP_200_OK)
		else:
			return Response({'message':"Some error occured while placing order."},status=status.HTTP_400_BAD_REQUEST)
