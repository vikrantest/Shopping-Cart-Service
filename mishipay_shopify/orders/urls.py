
from django.conf.urls import url
from orders.views import OrderView , CartView ,CartCheckoutView


urlpatterns = [
    url(r'^orders/', OrderView.as_view()),
    url(r'^cart/', CartView.as_view()),
    url(r'^cart/addproduct/', CartView.as_view()),
    url(r'^cart/removeproduct/', CartView.as_view()),
    url(r'^order-checkout/', CartCheckoutView.as_view()),
]
