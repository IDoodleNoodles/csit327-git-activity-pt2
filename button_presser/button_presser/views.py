
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def dashboard(request):
	return render(request, 'dashboard.html')

def login_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			messages.error(request, 'Invalid username or password')
	return render(request, 'login.html')

def register_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		if User.objects.filter(username=username).exists():
			messages.error(request, 'Username already exists')
		else:
			user = User.objects.create_user(username=username, email=email, password=password)
			login(request, user)
			return redirect('dashboard')
	return render(request, 'register.html')
