from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from .models import  trainer_availability

@receiver(post_save, sender=User)
def add_trainer_time(sender, instance, **kwargs):
	

	if instance.is_trainer == True:

		check_trainer_existance = trainer_availability.objects.filter(trainer=instance)

		if len(check_trainer_existance) == 0 :
			trainer_availability.objects.create(trainer=instance,available = '20:00')
			trainer_availability.objects.create(trainer=instance,available = '21:00')
			trainer_availability.objects.create(trainer=instance,available = '22:00')
			trainer_availability.objects.create(trainer=instance,available = '8:00')
			trainer_availability.objects.create(trainer=instance,available = '9:00')

