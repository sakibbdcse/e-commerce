from django.urls import path
from app_shop import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/<int:pk>/', views.ProductDetails.as_view(), name='product-details'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
]
