from django.urls import path
from . import views
from .views import RoomList, BookingList

urlpatterns = [
	path('',views.home,name = 'home'),
	path('room_list/',RoomList.as_view(),name='RoomList'),
	path('booking_list/',BookingList.as_view(),name='BookingList'),
	path('BookRoom/',views.BookRoom,name = 'BookRoom'),
	
]
