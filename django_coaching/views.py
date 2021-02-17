from django.shortcuts import render

def index(request):
	return render(request,'index.html')


def contact_page(request):
	return render(request,'contact-us.html')