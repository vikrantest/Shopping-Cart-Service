
from django.conf.urls import url
from shopping_frontend.views import *


urlpatterns = [
    url(r'^products/', ProductView.as_view()),
    url(r'^signin/', Signin.as_view()),
    url(r'^signout/', SignOut.as_view()),
    url(r'^cart/', CartView.as_view()),
    url(r'^orders/', OrderView.as_view()),

]
