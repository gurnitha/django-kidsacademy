# apps/home/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'home/index.html')