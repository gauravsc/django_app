from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.

def list_view(request):
	context = {}

	context['data'] = [1, 2, 3]

	return render(request, "social_app/list_view.html", context)

def logout_view(request):
	logout(request)

	return render(request, "social_app/index.html")
