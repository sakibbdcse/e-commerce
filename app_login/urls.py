from django.urls import path
from app_login import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'),
]
