from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

	path('dashboard/',views.dashboard,name='dashboard'),
	path('schedule/',views.schedule,name='schedule'),
	path('meeting/',views.meeting_link,name='meeting_link'),
	path('payment-done/',views.payment_done,name='payment_done'),
	path('change_password/',views.change_password,name='change_password'),
	path('payment-confirmed/',views.student_confirm,name='payment_confirmed')

       ]