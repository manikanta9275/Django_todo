from django.contrib import admin
from django.urls import path
# from django.shortcuts import HttpResponse
from app.views import *

# def home(request):
#     # print("Home")
#     return HttpResponse("helllo")
    

urlpatterns = [
   path('' , home , name='home'), 
   path('login12/' , login1, name='login11'),
   path('signup12/' , signup1, name='signup11'),
   path('add-todo/' , add),
   path('delete-todo/<int:id>',dele),
   path('change-status/<int:id>/<str:status>',cha_sta),
   path('logout/' , signout ), 
]