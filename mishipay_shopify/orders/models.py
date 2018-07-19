from django.db import models
from usermgmt.models import UserTable
from common.utils import DatetimeUtil


# Create your models here.

class CommonBaseData(models.Model):
	created_on = models.IntegerField(blank=False,null=False)
	updated_on = models.IntegerField(blank=False,null=False)
	deleted_on = models.IntegerField()
	status = models.CharField(max_length=20)

	def save(self, *args, **kwargs):
		self.updated_on = DatetimeUtil.unixtime()
		if not self.created_on:
			self.created_on = DatetimeUtil.unixtime()
		else:
			super(CommonBaseData, self).save(*args, **kwargs)


class Cart(CommonBaseData):
	user_customer = models.ForeignKey(UserTable, related_name='user_carts')
	cart_id = models.CharField(max_length=100)
	item_count = models.IntegerField(default=0)
	cart_price = models.FloatField(default=0.00)
	cart_status = models.CharField(max_length=20)

	class Meta:
		db_table = 'mishipay_shoppingcart'


	def get_create_cart(self):
		return True



class CartProducts(CommonBaseData):
	user_cart = models.ForeignKey(Cart, related_name='cart_products')
	product_id = models.CharField(max_length=100)
	product_status = models.CharField(default='added', max_length=20)

	class Meta:
		db_table ='mishipay_shoppingcart_products'



class Orders(CommonBaseData):
	order_id = models.CharField(max_length=100)
	transaction_id = models.CharField(max_length=100)
	payment_method = models.CharField(default='offline',max_length=20)
	order_cart = models.ForeignKey(Cart, related_name='user_cart_orders')
	order_status = models.CharField(default='pending',max_length=20)
	order_completion_time = models.IntegerField()

	class Meta:
		db_table = 'mishipay_shopping_orders'

