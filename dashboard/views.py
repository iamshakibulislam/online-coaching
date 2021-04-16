from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .models import trainer_availability,student_info,trainer_link
from django.contrib import messages
import twocheckout
from twocheckout import TwocheckoutError
from django.http import HttpResponse,JsonResponse,Http404
import json
import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from accounts.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import auth
import hmac
import hashlib
import base64
import requests

@login_required(login_url='/accounts/login/')
def dashboard(request):

	contxx=[]
	if request.user.is_trainer == True :
		info=student_info.objects.filter(teacher__trainer__email = request.user.email)

		for x in info :
			name = x.student.first_name + '  ' + x.student.last_name
			date=x.next_date
			time=x.time.strftime("%-I.%M.%p")
			final_hour=''
			final_minute=''
			status= ''
			splited=time.split(".")
			final_hour=int(splited[0])-1
			final_minute=splited[1]
			if splited[2] == 'PM':
				status = 'AM'
				date=date+timedelta(days=1)
			else :
				status = 'PM'



			#time=timen+timedelta(hours=11)

			contxx.append({'name':name,'date':date,'time':str(final_hour)+': '+str(final_minute)+'  ' + str(status)})


	checkstudent=student_info.objects.filter(student=request.user,is_paid=True)

	if len(checkstudent) > 0 :
		checkstudent = checkstudent[0]
		teacher = checkstudent.teacher.trainer.first_name + ' ' + checkstudent.teacher.trainer.last_name
		date = checkstudent.next_date
		time = checkstudent.time.strftime("%-I.%M %p")
		mlink= trainer_link.objects.get(trainer=checkstudent.teacher.trainer).link
		contxx={'teacher':teacher,'date':date,'time':time,'lnk':mlink}


	return render(request,'dashboard/index.html',{'contx':contxx,'len':len(contxx)})

@login_required(login_url='/accounts/login/')
def schedule(request):
	if request.method == 'GET':
		time=trainer_availability.objects.all()
		times=[]
		try:
			cookie = request.COOKIES['time']
			
		except :
			cookie = 0


		for available_time in time:
			if available_time.students_number < 2:
				times.append(available_time.available.strftime("%-I.%M %p"))

		
		return render(request,'dashboard/schedule.html',{'available_time':times,'totaltimecount':len(times)})

def student_confirm(request):
	if request.method == 'GET' :

		#refno = request.GET['refno']
		
		try:
			selected_time = request.COOKIES['time']

		except :

			return HttpResponse('<h1>Time was not selected</h1>')
		#token = request.POST['token']
		#ch_name = request.POST['cc-name']
		'''
		if token == 'none':
			messages.info(request,'card information is not valid')
			return redirect('schedule')
		'''
		if selected_time == "no" :
			messages.info(request,'No time available for now . Contact support ')
			return redirect('schedule')

		else :
			time=trainer_availability.objects.all()
			found = False
			trainer_table_id = ''
			time_allocated = ''
			for available_time in time:
				if available_time.students_number < 2 and selected_time == available_time.available.strftime("%-I.%M %p"):
					found = True
					trainer_table_id = available_time.id
					time_allocated = available_time.available

					break
			if found==True:

				#2checkout api action starts here 
				'''
				twocheckout.Api.auth_credentials({
				'private_key': '7A0667BA-7B96-465D-BBFC-B9CC527ADF79',
				'seller_id': '250757877049',
				
				
				

					
					
							})

				params = {
					'merchantOrderId': str(request.user.id),
					'token': str(token),
					'currency': 'USD',
					'total': '299.00',
					'billingAddr': {
						'name': str(ch_name),
						'addrLine1': '1591 Ocala Street Orlando',
						'city': 'Orlando',
						'state': 'Florida',
						'zipCode': '32806',
						'country': 'USA',
						'email': str(request.user.email),
						'phoneNumber' : '444-555-6666'
					},
					'demo':True
					

					
				  


					
				}
				'''

				try:

					sommething='lol'
					'''
					vendor_code = "250797972054"
					key = "hd]Vg!3BC4tymw8x@)+S"
					curr_date=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
					algo = str(str(len(vendor_code))+str(vendor_code)+str(len(curr_date))+curr_date)

					crypto = hmac.new(b'hd]Vg!3BC4tymw8x@)+S', algo.encode('utf-8'),digestmod=hashlib.md5).hexdigest()
					req_header = {
					"accept":"application/json",
					"X-Avangate-Authentication":"code='{}'' date='{}'' hash='{}' ".format(vendor_code,curr_date,crypto),
					"OrderReference":str(refno)
					}



					result = requests.get('https://api.2checkout.com/rest/6.0/orders/'+str(refno),headers=req_header)

					confirmed_ref_no=int(json.loads(result.content)['RefNo'])
					'''

					
					
					if 1==1:


						trainer_table = trainer_availability.objects.get(id=int(trainer_table_id))



						nextdate=datetime.now()+timedelta(days=4)
						if trainer_table.students_number == 1:
							seldate=student_info.objects.get(teacher=trainer_table,time=time_allocated).next_date
							nextdate = seldate+timedelta(days=1)
						if nextdate.strftime("%w") == "4" and time_allocated.strftime("%-I.%M %p") in ["8.00 PM","9.00 PM","10.00 PM"]:
							nextdate = nextdate + timedelta(days=2)
						if nextdate.strftime("%w") == "5" and time_allocated.strftime("%-I.%M %p") in ["8.00 AM","9.00 AM"]:
							nextdate = nextdate + timedelta(days=2)



						student_info.objects.create(
							student = request.user,
							teacher = trainer_table,
							is_paid = False,
							amount = 299.00,
							time = time_allocated,
							expire_date = datetime.now()+timedelta(days=30),
							next_date = nextdate

							)

						trainer_table.students_number = trainer_table.students_number + 1
						trainer_table.save()
						messages.success(request,'Course started successfully ')
					
						return redirect('payment_done')

					else:

						messages.info(request,'Payment failed ! Try again later')
						return redirect('schedule')


				except :
					messages.info(request,'FAILED! contact support')
					return redirect('schedule')
				

				# this code will go inside try block above
				
					
					
					
					

					

				# end of insider code of try block

				


				#2checkout api action ends here

				

			else:

				messages.info(request,'This schedule is not available. Contact support')

				return redirect('schedule')

	return redirect('dashboard')



@login_required(login_url='/accounts/login/')
def payment_done(request):



	sel = get_list_or_404(student_info,student=request.user)[0]

	if sel.is_paid == False :
		sel.is_paid = True
		sel.save()

		return render(request,'dashboard/payment-done.html')

	else :

		raise Http404



def meeting_link(request):
	if request.method == 'GET' and request.user.is_trainer:
		t=''
		try:
			t=trainer_link.objects.get(trainer=request.user)

		except :
			pass

		return render(request,'dashboard/meeting-link.html',{'lnk':t})

		

	if request.method == 'POST':
		url=request.POST['url']

		try:
			tl=trainer_link.objects.get(trainer=request.user)
			tl.link=url
			tl.save()


		except trainer_link.DoesNotExist :

			trainer_link.objects.create(trainer=request.user,link=url)

		messages.info(request,'meeting link has been updated')
		return redirect('meeting_link')




def change_password(request):
	if request.method == 'GET':
		return render(request,'dashboard/change-password.html')


	if request.method == 'POST':

		curr_pass = request.POST['curr_pass']
		newpass1= request.POST['new_pass1']
		newpass2= request.POST['new_pass2']
		selu=User.objects.get(email=request.user.email)
		if selu.check_password(curr_pass) and newpass1==newpass2:
			sel=User.objects.get(email=request.user.email)
			sel.set_password(newpass1)
			sel.save()
			auth.logout(request)

			messages.info(request,'password changed !')
			return redirect('login_page')

		else:
			messages.info(request,'Password error ! try again')
			return redirect('change_password')

		return redirect('change_password')