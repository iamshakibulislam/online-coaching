from django.db import models


class curriculums(models.Model):
	topic = models.CharField(max_length=80)

	def __str_(self):
		return str(self.topic)
