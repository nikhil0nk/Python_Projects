from django.shortcuts import render
from account.models import *
# Create your views here.

def userdata(request):
	context = {}

	accounts = Account.objects.all()
	context['accounts'] = accounts

	return render(request, 'users.html',context)

def uid(request, num):
	context = {}
	
	accid = Account.objects.get(id = num)
	context['accid'] = accid

	return render(request, 'user.html', context)
	


