import uuid
import os
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin,Permission
from django.db import models

# Create your models here.

class UserTable(AbstractBaseUser):
	display_name = models.CharField(max_length=100)
	useremail = models.EmailField(unique=True)
	is_staff = models.BooleanField(default=False)

	class Meta:
		db_table = 'mishipay_baseuser'