import datetime
import time
import sys
import os
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import  permission_classes
from rest_framework import permissions
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import render
from django.contrib.auth import authenticate
from common.utils import DatetimeUtil
from usermgmt.models import UserToken
from usermgmt.utils import Validators




@permission_classes((permissions.AllowAny,))
class ShopifySignin(APIView):
	"""
	User signin
	"""

	def __init__(self):
		valid_guest_signup = False
		self.mandatory_fields = ['useremail','password']

	def post(self,request):
		request_data = request.data

		validators =  Validators()

		mandatory_fields_res = validators.mandatory_validation(self.mandatory_fields,request_data)

		error_message = "Invalid Login Credentials"

		if len(mandatory_fields_res) == 0:
			if not validators.email_validator(request_data.get('useremail','')):
				return Response({"error":error_message},status=status.HTTP_400_BAD_REQUEST)
			else:
				valid_login = self.validate_login_cred(request_data)
				if valid_login:
					token = self.get_set_token(request_data,valid_login)
					return Response({'message':"User loggedin successfully","token":token},status=status.HTTP_201_CREATED) 

		else:
			error_message = "Missing mandatory fields, "+mandatory_fields_res
			return Response({"error":error_message},status=status.HTTP_400_BAD_REQUEST)

		
			# return Response({"error":error_message},status=status.HTTP_400_BAD_REQUEST)

		return Response({"error":error_message},status=status.HTTP_400_BAD_REQUEST)


	def validate_login_cred(self,data):
		useremail , password = str(data.get('useremail','')).strip() , str(data.get('password','')).strip()

		webuser = authenticate(username = useremail , password = password)

		return webuser

	def get_set_token(self,data,user):
		token, created = UserToken.objects.get_or_create(user=user)
		if not created:
		# update the created time of the token to keep it valid
			token.created = DatetimeUtil.unixtime()
			token.save()
		return token.key


@permission_classes((permissions.IsAuthenticated,))
class ShopifySignout(APIView):
	"""
	User signin
	"""

	def post(self,request):
		if self.delete_token(request.user):
			return Response({'message':'Logged out successfully'},status=status.HTTP_200_OK)
		else:
			return Response({'error':'Some error occured while logging out '},status=status.HTTP_200_OK)

	def delete_token(self,user):
		try:
			token = UserToken.objects.get(user = user)
			token.delete()
			return True
		except:
			return False


class CustomAuthToken(ObtainAuthToken):

	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data,
										   context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = UserToken.objects.get_or_create(user=user)
		return Response({
			'token': token.key,
			'user_id': user.pk,
			'email': user.useremail
		})



