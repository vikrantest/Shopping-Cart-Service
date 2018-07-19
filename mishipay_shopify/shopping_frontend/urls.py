
from django.conf.urls import url
from usermgmt.views import ProductView


urlpatterns = [
    url(r'^products/', ShopifySignin.as_view()),

]
