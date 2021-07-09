
from re import search, template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .views import*
urlpatterns = [
    
    path('register/',views.signUp,name='register'),
    path('profile',views.profile,name='profile'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
]
