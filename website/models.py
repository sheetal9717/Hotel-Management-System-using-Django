from django.db import models
from django.conf import settings
# Create your models here.

# class Room(models.Model):
# 	ROOM_CATEGORIES={
# 		('YAC','AC'),
# 		('NAC', 'NON-AC'),
# 		('DEL','DELUXE'),
# 	}
# 	number = models.IntegerField()
# 	category = models.CharField(max_length=3,choices = ROOM_CATEGORIES)
# 	beds = models.IntegerField()
# 	def __str__(self):
# 		return f'{self.number} {self.category} with {self.beds}'

# class Booking(models.Model):
	# user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)