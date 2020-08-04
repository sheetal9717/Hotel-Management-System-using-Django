from django.db import models
from django.conf import settings

# Create your models here.
class Room(models.Model):
	# ROOM_CATEGORIES={
	# 	('YAC','AC'),
	# 	('NAC', 'NON-AC'),
	# 	('DEL','DELUXE'),
	# }
	number = models.IntegerField()
	# category = models.CharField(max_length=3,choices = ROOM_CATEGORIES)
	beds = models.IntegerField()
	capacity = models.IntegerField()
	price = models.IntegerField()
	available = models.CharField(max_length=3)  

	def __str__(self):
		return f'room number is {self.number} with 2 beds for {self.capacity} people'

class Booking(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	check_in = models.DateTimeField()
	check_out = models.DateTimeField()
	person = models.IntegerField()

	def __str__(self):
		return f'{self.user} has {self.room} from {self.check_in} to {self.check_out}'
