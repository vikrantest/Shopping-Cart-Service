from django.db import models
from usermgmt.models import UserTable
from common.utils import DatetimeUtil


# Create your models here.

class CommonBaseData(models.Model):
	created_on = models.IntegerField(blank=False,null=False)
	updated_on = models.IntegerField(blank=False,null=False)
	# deleted_on = models.IntegerField()
	status = models.CharField(max_length=20)

	def save(self, *args, **kwargs):
		self.updated_on = DatetimeUtil.unixtime()
		if not self.created_on:
			self.created_on = DatetimeUtil.unixtime()
		super(CommonBaseData, self).save(*args, **kwargs)


class Cart(CommonBaseData):
	user_customer = models.ForeignKey(UserTable, related_name='user_carts')
	cart_id = models.CharField(max_length=100)
	item_count = models.IntegerField(default=0)
	cart_price = models.FloatField(default=0.00)
	cart_status = models.CharField(max_length=20)

	class Meta:
		db_table = 'mishipay_shoppingcart'


	def save(self, *args, **kwargs):
		if not self.cart_id:
			self.cart_id = str(DatetimeUtil.unixtime())+self.user_customer.display_name.replace(' ','_')
		super(Cart, self).save(*args, **kwargs)

	def getProducts(self,serialized=False):
		if not serialized:
			return CartProducts.objects.filter(user_cart=self)
		else:
			return CartProducts.objects.filter(user_cart=self).values('product_title','product_quantity','product_price')

	def addProduct(self,product):
		CartProducts.objects.create(user_cart=self,product_id=product['product_id'],product_quantity=product['quantity'],product_price=product['price'],variant_id=product['variant_id'],product_title=product['title'])
		self.cart_price+=(float(product['price'])*int(product['quantity']))
		self.item_count+=int(product['quantity'])
		self.save()
		return True

	def removeProduct(self,p_id):
		try:
			cart_item = CartProducts.objects.get(id=p_id)
			self.cart_price-=(float(cart_item.product_price)*int(cart_item.product_quantity))
			self.item_count-=int(cart_item.product_quantity)
			self.save()
			cart_item.delete()
			return True
		except:
			return False


class CartProducts(CommonBaseData):
	user_cart = models.ForeignKey(Cart, related_name='cart_products')
	product_id = models.CharField(max_length=100)
	product_title = models.CharField(max_length=150)
	variant_id = models.CharField(max_length=100)
	product_quantity = models.IntegerField(default=1)
	product_price = models.FloatField(default=0.00)
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

	def setOrderMetaData(self):
		for product in self.order_cart.getProducts():
			order_meta_obj = CartOrderBaseData(customer_order=self)
			order_meta_obj.product_id = product.product_id
			order_meta_obj.variant_id = product.variant_id
			order_meta_obj.product_quantity = product.product_quantity
			order_meta_obj.save()

	def getProducts(self):
		return self.order_cart.getProducts(True)



	def save(self, *args, **kwargs):
		cart_id = self.order_cart.cart_id
		if not self.order_id:
			self.order_id = "MishOrder"+cart_id
		if not self.transaction_id:
			self.transaction_id = "TransactioIV-"+cart_id
		super(Orders, self).save(*args, **kwargs)


class CartOrderBaseData(CommonBaseData):
	customer_order = models.ForeignKey(Orders, related_name='user_orders_details')
	product_id = models.CharField(max_length=100)
	variant_id = models.CharField(max_length=100)
	product_quantity = models.IntegerField(default=1)

	class Meta:
		db_table = "mishipay_order_data"
		# abstract = True


