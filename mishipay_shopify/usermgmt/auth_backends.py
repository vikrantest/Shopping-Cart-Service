import threading
import sys
from django.contrib.auth.hashers import check_password
from django.core.mail.backends.smtp import EmailBackend
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from rest_framework.authtoken.views import ObtainAuthToken


User = get_user_model()

class WebUserEmailAuthBackend(ModelBackend):
	"""
	auth backend for login
	"""

	def authenticate(self,request,username=None,password=None):
		try:
			from usermgmt.models import UserTable
			try:webuser = UserTable.objects.get(useremail=username)
			except:
				return None
			# webuser = UserTable(useremail='vsingh1918@gmail.com',display_name='Vikrant Singh')
			
			# webuser.set_password('test')
			# webuser.save()
			if webuser:
				if not webuser.check_password(password):
					return None
			else:
				return None
			return webuser
		except User.DoesNotExist:
			return None


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