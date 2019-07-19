from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views

app_name = 'user'
urlpatterns = [
	#   built in django class login in view for log in page
	path('login/', LoginView.as_view 
		(template_name='user/login.html'), name='login'),
	# log out page
	path('logout/', views.logout_view, name='logout'),
	path('register/', views.register, name='register'),
	path('profile/<username>/', views.user_profile, name='profile'),
	path('profile/<username>/update/', views.user_profile_update, name='profile_update'),
]

