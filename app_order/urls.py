from django.urls import path
from app_shop import views as shop_views
from app_order import views as order_views

urlpatterns = [
    path('', shop_views.Home.as_view(), name='home'),
    path('product/<pk>/', shop_views.ProductDetails.as_view(), name='product-details'),
    path('add-to-cart/<pk>/', order_views.add_to_cart, name='add_to_cart'),
    path('cart/', order_views.cart_view, name='cart'),
]
