from django.shortcuts import render
from .models import trainer_availability
def dashboard(request):
	return render(request,'dashboard/index.html')


def schedule(request):
	if request.method == 'GET':
		time=trainer_availability.objects.all()
		times=[]

		for available_time in time:
			if available_time.students_number < 2:
				times.append(available_time.available.strftime("%-I.%M %p"))


		return render(request,'dashboard/schedule.html',{'available_time':times})


	if request.method == 'POST' :
		pass