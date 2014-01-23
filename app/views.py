from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from requests import *
from stripe import *
from forms import *
from models import User
import oauth2 as oauth

#for selector, pull user session from request, and authenticate, then render index with appropriate tier
def index(request):
	return render(request, 'index.html')

def login(request):
	user = User.objects.filter(email=request.POST.get('email'))
	user = authenticate(email=user.email, password=user.password)
	if user is not None:
		#login() begins session
		user.login(request, user)
		return redirect(index)

	else:
		return redirect('incorectLogin.html')

#validate form, save to db, add to appropriate group/permissions
def createUser(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			#tier will be a hidden tickbox, chosen by form UI
			user = User.objects.create_user(email=form.cleaned_data['email'], 
												first_name=form.cleaned_data['first_name'],
												last_name=form.cleaned_data['last_name'],
												password=form.cleaned_data['password'],
												tier=request.POST.get('tier'),
												token = request.POST.get('stripe_token')
												)

	else:
		form = NewUserForm()
	
	return render(request, 'createUser.html', {'form':form})

#given user object, user.set_password(password), user.save()
def changePassword(request):
	return render(request, 'changePassword.html')

def discussionBoard(request):
	return render(request, 'discussion.html')

def logout(request):
	#pull user from session, logout()
	logout(request)
	return render(request, 'logout.html')