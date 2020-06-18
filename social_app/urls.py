from django.urls import path
from .views import list_view, logout_view

urlpatterns = [
	path('stories', list_view),
	path('logout', logout_view)
]
    