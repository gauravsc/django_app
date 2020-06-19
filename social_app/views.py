from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from social_app.models import Spreadsheets
from datetime import datetime

# Create your views here.

def list_view(request):
	context = {}

	context['current_spreadsheet'] = "{'name':'Gaurav'}"

	return render(request, "social_app/list_view.html", context)


def post_submission(request):
	if request.method == 'POST':
		spreadsheet = request.POST['spreadsheet']

	data_to_save = Spreadsheets(user=request.user,
		upvotes=2,
		spreadsheet_json=spreadsheet,
		pub_date=datetime.now()
		)
	data_to_save.save()

	return render(request, "social_app/thank.html")



def logout_view(request):
	logout(request)

	return render(request, "social_app/index.html")
