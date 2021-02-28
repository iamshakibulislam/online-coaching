from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .models import trainer_availability,student_info
from django.contrib import messages
import twocheckout
from twocheckout import TwocheckoutError
from django.http import HttpResponse,JsonResponse,Http404
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
		token = request.POST['token'].replace('-','')
		ch_name = request.POST['cc-name']
		
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

				try:

					result = twocheckout.Charge.authorize(params)
					print(result)
					if result.responseCode == 'APPROVED':


						trainer_table = trainer_availability.objects.get(id=int(trainer_table_id))
						student_info.objects.create(
							student = request.user,
							teacher = trainer_table,
							is_paid = False,
							amount = 299.00,
							time = time_allocated,
							expire_date = datetime.now()+timedelta(days=28)

							)

						trainer_table.students_number = trainer_table.students_number + 1
						trainer_table.save()
						messages.success(request,'Course started successfully ')
					
						return redirect('payment_done')

					else:

						messages.info(request,'Payment failed ! Try again later')
						return redirect('schedule')



				except TwocheckoutError as error :
					messages.info(request,'Payment error | Try again later')
					return redirect('schedule')

				# this code will go inside try block above
				
					
					
					
					

					

				# end of insider code of try block

				


				#2checkout api action ends here

				

			else:

				messages.info(request,'This schedule is not available. Try again please')

				return redirect('schedule')

	return redirect('dashboard')




def payment_done(request):



	sel = get_list_or_404(student_info,student=request.user)[0]

	if sel.is_paid == False :
		sel.is_paid = True
		sel.save()

		return render(request,'dashboard/payment-done.html')

	else :

		raise Http404

