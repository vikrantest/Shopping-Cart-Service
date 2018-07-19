import uuid
import os
import binascii
from django.conf import settings as my_settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin,Permission
from django.db import models
from common.utils import DatetimeUtil

User = my_settings.AUTH_USER_MODEL

class UserTable(AbstractBaseUser):
	display_name = models.CharField(max_length=100)
	useremail = models.EmailField(unique=True)
	is_staff = models.BooleanField(default=False)
	USERNAME_FIELD = 'useremail'
	REQUIRED_FIELDS = ['display_name']

	class Meta:
		db_table = 'mishipay_baseuser'


class UserToken(models.Model):
	created_on = models.IntegerField()
	updated_on = models.IntegerField()
	deleted_on = models.IntegerField(null=True, blank=True)
	key = models.CharField(max_length=50, primary_key=True)
	user = models.OneToOneField(UserTable, related_name='user_auth_token',on_delete=models.CASCADE)

	class Meta:
		db_table = 'auth_token'


	def save(self, *args, **kwargs):
		self.updated_on = DatetimeUtil.unixtime()
		if not self.created_on:
			self.created_on = DatetimeUtil.unixtime()
		if not self.key:
			self.key = self.generate_key()
		return super(UserToken, self).save(*args, **kwargs)

	def generate_key(self):
		return binascii.hexlify(os.urandom(20)).decode() #change key generation mechanism

	def __str__(self):
		return self.key