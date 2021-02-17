from django.shortcuts import render


def login_page(request):
	if request.method == 'GET':
		return render(request,'login.html')


def registration_page(request):

	if request.method == 'GET':
		return render(request,'registration.html')