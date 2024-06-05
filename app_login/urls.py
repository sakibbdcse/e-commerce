from django.urls import path
from app_login import views
urlpatterns = [
    path('sigin-up/', views.sign_up, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]