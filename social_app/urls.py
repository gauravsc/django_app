from django.urls import path
from .views import list_view, logout_view, post_submission

urlpatterns = [
	path('stories', list_view),
	path('logout', logout_view),
	path('post_submission', post_submission)
]
    