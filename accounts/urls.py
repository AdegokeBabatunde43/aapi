from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.signin, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout', views.signout, name='logout'),
]