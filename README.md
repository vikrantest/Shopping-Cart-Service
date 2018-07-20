# Shopping-Cart-Service

To create a web based server which pulls product information from a Shopify based POS
system and updates inventory every time a sale is made.

Features - 

1. Create web based server (Use a framework of your choice).
2. Integrate with Shopify to retrieve product information from the inventory.
3. Integrate with Shopify to create an Order on the system.
4. Demonstration using a web page.
5. Authentication for user (Login).


REST API - 


TEST Login - "useremail":"vsingh1918@gmail.com",
              "password":"test"


/api/v1/products/ 
  API -  List all products
  Auth - No auth allow
  Method - GET
  Data - None
  
/api/v1/cart/
  API -  List all products in CART
  Auth - Auth Required
  Method - GET
  Data - None
  
/api/v1/cart/addproduct/
  API -  Add a products in CART
  Auth - Auth Required
  Method - PUT
  Data - None
  
/api/v1/removeproduct/
  API -  Remove a products in CART
  Auth - Auth Required
  Method - DELETE
  Data - None
  
/api/v1/order-checkout/
  API -  Checkout Your Cart
  Auth - Auth Required
  Method - POST
  Data - None
  
/api/v1/orders/
  API -  List all your orders with product
  Auth - Auth Required
  Method - GET
  Data - None
  
/api/v1/user/sign-in/
  API -  Sign in 
  Auth - Auth Not Required
  Method - POST
  Data - {"useremail":"vsingh1918@gmail.com","password":"test"}
  
/api/v1/user/sign-out/
  API -  Sign out from APP
  Auth - Auth Required
  Method - POST
  Data - None
  
/api/v1/user/obtain_token/



Frontend URLs

/webapp/products/ - Product Listing on WEBAPP                                               
/webapp/orders/ - Order listing on WEBAPP                                                             
/webapp/cart/ - Display Cart Page in WEBAPP                                                         
/webapp/signin - Signin WEBAPP using token from API service                                           
/webapp/signout - Signout from WEBAPP                                                         
