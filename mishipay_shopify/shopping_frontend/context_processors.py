import json
import os

token_file = os.getcwd()+"/shopping_frontend/token.json"

def loggedin(request):
	with open(token_file,"r") as token_obj:
		data = json.load(token_obj)
	return {"loggedin_token":data.get('token',None)}