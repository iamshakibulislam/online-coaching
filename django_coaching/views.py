from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from dashboard.models import contact_messages
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def index(request):
	return render(request,'index.html')

@xframe_options_exempt
def contact_page(request):
	if request.method == 'GET':
		return render(request,'contact-us.html')

	if request.method == 'POST':
		email=request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		contact_messages.objects.create(email=email,subject=subject,message=message)
		messages.info(request,'message sent successfully ! we will get back to you soon.')
		return redirect('contact_page')


