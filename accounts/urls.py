 

from django.urls import path
from . import views

urlpatterns = [
  
  	path('login/',views.login_page,name='login_page'),
    path('register/',views.registration_page,name='registration_page'),

]

 