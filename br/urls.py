
from re import search
from django.urls import path
from . import views
from .views import*
urlpatterns = [
    
    path('br/',views.home,name='b_request'),

    
]
