
from re import search
from django.urls import path
from . import views
from .views import*
urlpatterns = [
    
    path('',views.home,name='home'),
    path('doner',views.add_blood_doner,name='doner'),
    path('create_post',views.blood_request_post,name='create'),
    path('request',views.all_blood_request_list,name='request'),
    path('details/<int:id>',views.all_blood_request_detail,name='details'),
    path('delete/<int:id>',views.delete_request_post,name='delete_post'),
    path('update/<int:id>',views.update_request_post,name='update_post'),
    # path('doner_list',views.search_doner,name='doner_list'),
    path('search',views.doner,name='doner_list'),
    path('add_hospital',views.add_hospital_ambulance,name='add_hospital'),
    # path('hospital',views.hospital_and_ambulance_search,name='hospital'),
    path('add_ambulance',views.add_ambulance,name='add_ambulance'),
    path('ambulance',views.ambulance_search,name='ambulance'),
    path('request_list/<int:id>',views.blood_request_post_detail,name='post_request'),
    path('hospital',views.hospital,name='hospital')


    
]
