from django.shortcuts import render,redirect
from .models import trainer_availability,student_info
from django.contrib import messages
import twocheckout
from twocheckout import TwocheckoutError
from django.http import HttpResponse,JsonResponse
import json
import datetime
from datetime import datetime, timedelta


def dashboard(request):
	return render(request,'dashboard/index.html')


def schedule(request):
	if request.method == 'GET':
		time=trainer_availability.objects.all()
		times=[]

		for available_time in time:
			if available_time.students_number < 2:
				times.append(available_time.available.strftime("%-I.%M %p"))


		return render(request,'dashboard/schedule.html',{'available_time':times,'totaltimecount':len(times)})


	if request.method == 'POST' :
		
		selected_time = request.POST['time']
		token = request.POST['token']
		
		if token == 'none':
			messages.info(request,'card information is not valid')
			return redirect('schedule')

		if selected_time == "no" :
			messages.info(request,'No time available for now . Try again tomorrow')
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

				twocheckout.Api.auth_credentials({
   				 'private_key': '7A0667BA-7B96-465D-BBFC-B9CC527ADF79',
    				'seller_id': '250757877049',
    				
    				
							})

				params = {
				    'merchantOrderId': '5',
				    'token': token,
				    'currency': 'USD',
				    'total': '299.00',
				    'billingAddr': {
				        'name': 'shail',
				        'addrLine1': '123 test',
				        'city': 'Columbus',
				        'state': 'OH',
				        'zipCode': '43123',
				        'country': 'USA',
				        'email': 'demoemail@gmail.com',
				        'phoneNumber' : '555-555-5555'
				    }


				    
				}

				try:
				    result = twocheckout.Charge.authorize(params)
				    return redirect('dashboard')

				except TwocheckoutError as error :
					print(error.msg)

				# this code will go inside try block above
				trainer_table = trainer_availability.objects.get(id=int(trainer_table_id))
				student_info.objects.create(
					student = request.user,
					teacher = trainer_table,
					is_paid = True,
					amount = 299.00,
					time = time_allocated,
					expire_date = datetime.now()+timedelta(days=28)


					)

				trainer_table.students_number = trainer_table.students_number + 1
				trainer_table.save()
				messages.success(request,'Course started successfully ')


				# end of insider code of try block

				return redirect('schedule')


				#2checkout api action ends here

				

			else:

				messages.info(request,'This schedule is not available. Try again please')

				return redirect('schedule')




