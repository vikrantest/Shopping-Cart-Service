from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from usermgmt.models import UserToken

class CustomTokenAuthentication(TokenAuthentication):
	"""
	token authentication backend
	"""
	model = UserToken

	def authenticate_credentials(self, key):
		try:
			token = UserToken.objects.select_related('user').get(key=key)
		except self.model.DoesNotExist:
			raise exceptions.AuthenticationFailed('Authentication failed') 

		if not token.user.is_active:
			raise exceptions.AuthenticationFailed('User inactive or deleted')

		return (token.user, token)

