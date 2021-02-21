from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
import requests
from accounts.models import User
from django.contrib import auth




def login_page(request):
	if request.method == 'GET':
		return render(request,'login.html')

	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']

		authenticate=auth.authenticate(request,email=email,password=password)
		if authenticate is not None :
			auth.login(request,authenticate)

			return redirect('dashboard')

		else:
			return render(request,'login.html',{'message':'username or password is incorrect !'})


def registration_page(request):

	if request.method == 'GET':
		return render(request,'registration.html')


	if request.method == 'POST' :

		first_name = request.POST['first-name']
		last_name = request.POST['last-name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 != password2 :

			return render(request,'registration.html',{'passerror':'password did not match !'})


		else:
				try:
					User.objects.get(email=email)

					return render(request,'registration.html',
						{'userexist':'user aready exists'})
				except User.DoesNotExist:
					User.objects.create_user(password=password1,first_name=first_name,email=email,
						last_name=last_name)
					return render(request,'registration.html',
						{'success':'account created successfully.You can <a href="#">login </a> now'})

