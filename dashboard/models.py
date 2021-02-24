from django.db import models
from accounts.models import User

class curriculums(models.Model):
	topic = models.CharField(max_length=80)

	def __str__(self):
		return str(self.topic)

	class Meta :
		verbose_name='django course curriculums'
		verbose_name_plural='curriculum'

class trainer_availability(models.Model):
	trainer = models.ForeignKey(User, on_delete=models.CASCADE)
	available = models.TimeField(auto_now=False,auto_now_add=False)
	students_number = models.IntegerField(null=True,default=0)

	class Meta:
		verbose_name='trainers availability'
		verbose_name_plural = 'trainers'



	def __str__(self):
		return str(self.trainer.first_name+'  '+self.trainer.last_name +'  '+'email:'+'  '+self.trainer.email)


class student_info(models.Model):
	student = models.ForeignKey(User,on_delete=models.CASCADE)
	teacher = models.ForeignKey(trainer_availability,on_delete=models.CASCADE)
	is_paid = models.BooleanField(default=False)
	amount = models.FloatField(default=0,null=False)
	time = models.TimeField(auto_now_add=False,auto_now=False)

	class Meta:
		verbose_name='student information'
		verbose_name_plural='studends information'


	def __str__(self):
		return str(self.student.first_name + '   ' + self.student.last_name)





