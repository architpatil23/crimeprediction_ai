from django.http import HttpResponse
from django.shortcuts import render
def about(request):
	#return HttpResponse('about')
	return render(request,'aboutus.html')

def homepage(request):
	#return HttpResponse('WelcomeHome')
	return render(request, 'home_template/startbootstrap-agency/index.html')