import json
import requests
import os

token_file = os.getcwd()+"/shopping_frontend/token.json"

class RequestUtility:
	DOMAIN = 'http://127.0.0.1:8000'
	URLS = {"login":"/api/v1/user/sign-in/","logout":"/api/v1/user/sign-out/","get_cart":"/api/v1/cart/","get_orders":"/api/v1/orders/"}

	def __init__(self):

		self.EVENT_API_HANDLER = {"login":self.loginAPI,"logout":self.logoutAPI,"get_cart":self.getCartAPI,"get_orders":self.getOrderAPI}

	def __call__(self,event,data=None):
		if event == 'login':
			return self.EVENT_API_HANDLER[event](data)
		else:
			return self.EVENT_API_HANDLER[event]()

	def makeAPICall(self,url,data,method,headers=None):
		if method == "POST":
			return requests.post(url,data=data,headers=headers)
		elif method == "GET":
			return requests.get(url,data=data,headers=headers)

	def getHeader(self):
		def get_token():
			with open(token_file,"r") as token_obj:
				data = json.load(token_obj)
			return data.get('token','')
		return {"Authorization":"Token "+get_token()}

	def loginAPI(self,data):
		data = {"useremail":data["useremail"],"password":data["password"]}
		url = RequestUtility.DOMAIN+RequestUtility.URLS["login"]

		response_data = self.makeAPICall(url,data,'POST',None)
		return response_data.json()

	def logoutAPI(self):
		url = RequestUtility.DOMAIN+RequestUtility.URLS["logout"]
		response_data = self.makeAPICall(url,None,'POST',self.getHeader())
		return response_data.json()

	def getCartAPI(self):
		url = RequestUtility.DOMAIN+RequestUtility.URLS["get_cart"]
		response_data = self.makeAPICall(url,None,'GET',self.getHeader())
		return response_data.json()

	def getOrderAPI(self):
		url = RequestUtility.DOMAIN+RequestUtility.URLS["get_orders"]
		response_data = self.makeAPICall(url,None,'GET',self.getHeader())
		return response_data.json()





class BackendAPIUtils:

	@staticmethod
	def signin(data):
		util_obj = RequestUtility()
		response = util_obj("login",data)
		if response.get("message"):
			with open(token_file,"w") as token_obj:
				json.dump({"token":response.get("token","")}, token_obj)
			return True , response.get("token")
		return False,""

	@staticmethod
	def signout():
		util_obj = RequestUtility()
		response = util_obj("logout")
		if response.get("message"):
			with open(token_file,"w") as token_obj:
				json.dump({}, token_obj)
			return True 
		return False

	@staticmethod
	def getCart():
		util_obj = RequestUtility()
		response = util_obj("get_cart")
		return response

	@staticmethod
	def getOrders():
		util_obj = RequestUtility()
		response = util_obj("get_orders")
		return response

