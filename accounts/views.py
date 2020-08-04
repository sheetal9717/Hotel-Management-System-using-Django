from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from website import views

def login(request):
	if request.method == "POST":
		uname = request.POST['username']
		pwd = request.POST['password']
		user = auth.authenticate(username=uname,password=pwd)
		if user is not None: 
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request,'login.html',{'error': "Invalid Login credentials."})
	else:
		return render(request,'login.html',{})


def register(request):
	if request.method == "POST":
		if request.POST['password'] == request.POST['passwordagain']:
			try:
				user = User.objects.get(username=request.POST['username'])
				# user = User.objects.get(email=request.POST['email'])
				return render(request,'register.html',{'error':"Username has already been taken"})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
				auth.login(request,user),
				return redirect('home')
				
		else:
			return render(request,'register.html',{'error':"Password don't matches"})
	else:
		return render(request,'register.html',{})


# def logout(redirect):
# 	auth.logout(request)
# 	return render('home')
#
# call this ,method in any html file as :
# 	<a href="{% url 'logout'%}"></a>
#and include this method in urls.py as: path('logout/',views.logout,name = 'logout'),
 