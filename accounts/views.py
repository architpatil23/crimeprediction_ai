# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			# login karlo frans
			login(request,user)
			return redirect('accounts:profile')

	else:
		form = UserCreationForm()
	return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log user in
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('/')
	else:
		form = AuthenticationForm()
	return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/')
	logout(request)
	return redirect ('/')

@login_required(login_url="/accounts/login/")
def profile_view(request):
	return render(request,'accounts/profile_template/profilepage.html')
