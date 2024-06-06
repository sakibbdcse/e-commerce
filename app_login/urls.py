from django.urls import path
from django.contrib.auth import views as auth_views
from app_login import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('profile/', views.user_profile, name='profile'),
]
