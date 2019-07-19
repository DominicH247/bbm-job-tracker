from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from jobs.models import Job


def logout_view(request):
	"""log user out and redirect to job list page """
	logout(request)
	return redirect('job_list')

def register(request):
	"""register new user"""
	if request.method == "POST": 
		#  process the filled in form
		form = CustomUserCreationForm(data=request.POST)
		if form.is_valid():
			# save form 
			new_user = form.save()
			# log the user in and redirect to home page
			authenticated_user = authenticate(
				username=new_user.username,
				password = request.POST['password1'])
			login(request, authenticated_user)
			return redirect ('job_list')
	else:
		#  display blank form
		form = CustomUserCreationForm()

	context = {'form':form}
	return render(request, 'user/register.html', context)

@login_required
def user_profile(request, username):
	"""display user profile page"""
	#  get user info
	user = CustomUser.objects.get(username=username)
	#  get user job info
	user_jobs = Job.objects.filter(author=user) 
	# count of jobs created by user
	user_job_count = user_jobs.count()
	context = {
		'user':user,
		'user_jobs':user_jobs,
		'user_job_count':user_job_count,
	}
	return render(request,'user/profile.html', context)

@login_required
def user_profile_update(request, username):
	"""user update info page"""
	user = CustomUser.objects.get(username=username)
	#  must be original author to update the job
	if user != request.user:
		raise Http404
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance=user)
		if form.is_valid():
			update_profile = form.save(commit=False)
			update_profile.save()
			return redirect ('user:profile',username=username)
	else: 
		#  pre-fill form with current entry
		form = CustomUserChangeForm(instance=user)
	context = {
		'user':user,
		'form':form
		}
	return render(request, 'user/profile_update.html', context)







