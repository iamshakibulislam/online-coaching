from django.shortcuts import render

def dashboard(request):
	return render(request,'dashboard/index.html')


def schedule(request):
	if request.method == 'GET':
		return render(request,'dashboard/schedule.html')