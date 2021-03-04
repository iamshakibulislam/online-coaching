from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  
  	path('login/',views.login_page,name='login_page'),
  	path('logout/',views.logout,name='logout'),
    path('register/',views.registration_page,name='registration_page'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='registration/reset.html',
    	html_email_template_name='registration/password-reset-email-template.html'),name='password_reset'),
	path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/reset-done.html'),
		name='password_reset_done'),
	path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset-conf.html'),
		name='password_reset_confirm'),
	path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset-suc.html'),
		name='password_reset_complete'),

]

 