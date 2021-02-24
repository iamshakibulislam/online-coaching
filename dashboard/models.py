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



	def __str__(self):
		return str(self.trainer.first_name)
