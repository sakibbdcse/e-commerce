from django.urls import path
from app_order import views

urlpatterns = [
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
]
