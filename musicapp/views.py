from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context = ['demo1','demo2','demo3']
	return render(request,'musicapp/index.html')