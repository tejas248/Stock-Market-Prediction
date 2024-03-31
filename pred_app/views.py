from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import  authenticate
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from pred_app.lstm_prediction import *

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
import Send__email

# --------------- MAIN WEB PAGES -----------------------------
def redirect_root(request):
    return redirect('/pred_app/index')

def index(request):
	return render(request, 'pred_app/index.html') 

def pred(request):
    return render(request, 'pred_app/prediction.html')

def signup(request):
	if request.method == 'GET':
		return render(request, 'pred_app/signup_user.html')
	else:
		username = request.POST['username'] 
		password1 = request.POST['password1'] 
		password2 = request.POST['password2'] 
		if (len(username)==0 or len(password1)==0 or len(password2)==0 ):
			return render(request, 'pred_app/signup_user.html', {'error':'Consider all fields'})
		else:
			if(password1 == password2):
				try:
					user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
					user.save()
					return render(request, 'pred_app/login_user.html')
				except:
					return render(request, 'pred_app/signup_user.html', {'error':'That username has already been taken. Please choose a new username'})
			else:
				return render(request, 'pred_app/signup_user.html', {'error':'Password did not matched'})


def login(request):
	if request.method == 'GET':
		return render(request, 'pred_app/login_user.html', {'form':AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			print('no exist')
			return render(request, 'pred_app/login_user.html', {'form':AuthenticationForm(),'error':'Username and password did not match'})
		else:
			print('Login')
			auth_login(request, user)
			return redirect('/pred_app/index')
		# return render(request, 'pred_app/login_user.html')


@login_required
def logout(request):
	if request.method == 'POST':
		auth_logout(request)
		return render(request, 'pred_app/index.html') 


def contact(request):
	if request.method == 'GET':
		return render(request, 'pred_app/contact.html')
	else:
		name = request.POST['username'] 
		email = request.POST['email'] 
		message = request.POST['message']
		print(name)
		print(email)
		print(message)

		Send__email.send(subject='Feedback Message acknowledgement',send_to=email,message=message)
		return render(request, 'pred_app/contact.html',{'error':"Thank You for submitting your Feedback"})



def search(request, se, stock_symbol):
	import json
	predicted_result_df = lstm_prediction(se, stock_symbol)
	return render(request, 'pred_app/search.html', {"predicted_result_df": predicted_result_df})
# -----------------------------------------------------------