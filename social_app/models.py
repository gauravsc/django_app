from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Spreadsheets(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	upvotes = models.IntegerField(default=0)
	spreadsheet_json = models.CharField(max_length=2000)
	pub_date = models.DateTimeField('date published')


# user = User.objects.get(id=2)
# s = Spreadsheets(user=user, upvotes=2, spreadsheet_json='{}', pub_date='1950-01-01')