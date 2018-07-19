
from django.conf.urls import url
from usermgmt.views import ShopifySignin , ShopifySignout , CustomAuthToken
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^sign-in/', ShopifySignin.as_view()),
    url(r'^sign-out/', ShopifySignout.as_view()),
    url(r'^obtain_token/', CustomAuthToken.as_view()),

]
