from .models import *
from datetime import datetime,timedelta

def class_schedule():

	student_list = student_info.objects.all()

	for student in student_list:

		if student.expire_date == datetime.now() :
			trainer_user = student.teacher.trainer
			sel_trainer=trainer_availability.objects.get(trainer = trainer_user)
			sel_trainer.students_number = sel_trainer.students_number - 1
			sel_trainer.save()
			student.delete()


		nextdate=student.next_date+timedelta(days=2)


		if nextdate.strftime("%w") == "4" and student.time.strftime("%-I.%M %p") in ["8.00 PM","9.00 PM","10.00 PM"]:

			student.next_date = nextdate + timedelta(days=2)
			student.save()


		if nextdate.strftime("%w") == "5" and student.time.strftime("%-I.%M %p") in ["8.00 AM","9.00 AM"]:

			student.next_date = nextdate + timedelta(days=2)
			student.save()





	