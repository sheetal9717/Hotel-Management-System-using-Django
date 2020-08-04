from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView
from accounts.models import Room, Booking
import datetime
import pytz
# Create your views here.

def home(request):
	return render(request,'home.html',{})

class RoomList(ListView): #to see room list
	model = Room


class BookingList(ListView):# to see booking list
	model = Booking
 

def check_availability(room, check_in, check_out):
	avail_list =[]
	Booking_list = Booking.objects.filter(room = room)

	check_in = pytz.utc.localize(check_in)
	check_out = pytz.utc.localize(check_out)

	for booking in Booking_list:
		print(booking.check_in)
		print(booking.check_out)
		if booking.check_in>check_out or booking.check_out<check_in:
			avail_list.append(True)
		else:
			avail_list.append(False)
	# print("________________________")
	return all(avail_list)


def BookRoom(request):
	if request.method == "POST":
		Check_in = request.POST['checkin']
		Check_out = request.POST['checkout']
		person = request.POST['person']
		person = int(person)
		# print(type(person))
		Check_in = datetime.datetime.strptime(Check_in, '%d %b %Y')
		Check_out = datetime.datetime.strptime(Check_out, '%d %b %Y')
		
		available_room = []
		room_detail = Room.objects.all() #to get room table
		# print(room_detail)
		for room in room_detail:
			res = check_availability(room, Check_in, Check_out) #check available room
			if res == True:
				available_room.append(room)

		if len(available_room)>0:
			room = available_room[0]
			room.available = "No" #set room availability as not available
			booking_details = Booking.objects.create( 
				user = request.user,
				room = room,
				check_in = Check_in,
				check_out = Check_out,
				person = person)
			booking_details.save() # save booking detail to the database
			return HttpResponse(booking_details)
		else:
			return HttpResponse("Room isn't available.")
	else:
		return render(request,'home.html',{})





