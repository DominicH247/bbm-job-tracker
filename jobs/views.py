from django.shortcuts import render, redirect
from .models import Job, Objective
from user.models import CustomUser
from comments.models import Comment

from .forms import JobCreateForm, ObjectiveCreateForm
from django.forms import inlineformset_factory
from comments.forms import UserCommentForm, ObjectiveCommentForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator
from comments.utils import notify_job_auth_comment, notify_job_personnel_comment
from datetime import date
from .utils import Deadline

#  users must be logged in to view the pages @login_required
#  decorators have been used

@login_required 
def job_list(request):
	"""displays all active jobs"""
	jobs = Job.objects.order_by('-created_date')  # most recent at top
	job_count = Job.objects.count()  # count of all jobs
	paginator = Paginator(jobs, 15)  # paginator 10 objects per view
	page = request.GET.get('page') # paginator
	jobs = paginator.get_page(page) # paginated object
	context = {
		'jobs':jobs,
		'job_count':job_count,
		}
	return render(request, 'jobs/job_list.html', context)

@login_required 
def job_list_open(request):
	"""displays page of open job stauses"""
	job_query = Job.objects.filter(job_status__icontains="open")
	jobs = job_query.order_by('-created_date')
	job_open_count = job_query.count()  # clount of open jobs
	context = {
		'jobs':jobs,
		'job_open_count':job_open_count,
		}
	return render(request, 'jobs/job_list_open.html', context)

@login_required 
def job_list_closed(request):
	"""displays list of closed jobs"""
	job_query = Job.objects.filter(job_status__icontains="closed")
	jobs = job_query.order_by('-created_date')
	job_closed_count = job_query.count()
	context = {
		'jobs':jobs,
		'job_closed_count':job_closed_count,
		}
	return render(request, 'jobs/job_list_closed.html', context)


@login_required 
def job_detail(request, job_details_id):
	"""job detail view with integrated user comment form"""
	try:
		job_details = Job.objects.get(pk=job_details_id)
		comments = job_details.comments.all()
		objectives = job_details.objectives.all()
		deadline = Deadline(job_details)
		# objectives = job.details.objective_comments.all()
		#  return  all personnel in jobs (m2m) as list for notifications
		#  for m2m field rtn as related object manager not iterable
		#  must use .all() to convert it to a queryset
		# personnel = list(job_details.personnel.all())
	
		#  user comment form 
		if request.method == 'POST':
			form = UserCommentForm(request.POST)
			if form.is_valid():
				user_comment = form.save(commit=False)
				#  to link comment to the job through ForeignKey relationship 
				#  need to assign job model instance when saving comment model instance
				user_comment.job = job_details
				user_comment.comment_by = request.user
				user_comment.save()
				#  notify job author of comment 
				notify_job_auth_comment(
					user_comment.comment_by, 
					job_details.author,
					sender = user_comment.comment_by,
					recipient = job_details.author,
					verb = "commented",
					target = job_details
					)
				#  notify personel associated to job when user comments
				#  exclude commentor from recieving notification if he made the comment
				personnel_list = job_details.personnel.exclude(id = request.user.id)
				notify_job_personnel_comment(
					sender = user_comment.comment_by,
					recipient = personnel_list,
					verb = "commented",
					target = job_details
					)

				return redirect('job_detail', job_details_id=job_details.id)
		else:
			#  deadline checker arguements job id and job deadline 
			deadline_context = deadline.check_deadline()
			form = UserCommentForm()
			paginator = Paginator(comments, 5) # paginator 10 objects per view
			page = request.GET.get('page')  # paginator
			job_details_pag = paginator.get_page(page)  # paginated object
			context = {
			'job_details':job_details,
			'objectives':objectives,
			'job_details_pag':job_details_pag,
			'deadline_context':deadline_context,
			'form':form
			}	
		return render(request, 'jobs/job_detail.html', context)
	except Job.DoesNotExist:
		raise Http404("Job does not exist")
		
@login_required 
def job_create(request):
	"""Job creation view with form"""
	#  if this is a POST request we need to process the form data 
	if request.method == 'POST':
		#  create a form instance and populate it with data from the request:
		form = JobCreateForm(request.POST, request = request)
		# objective_form = ObjectiveCreateForm(request.POST)
		#  check whether form data is valid:
		
		# if form.is_valid() and objective_form.is_valid():
		if form.is_valid():
			#  process the data in the form.cleaned_data as required
			new_job = form.save(commit=False)
			new_job.author = request.user
			# new_objective = objective_form.save(commit=False)
			new_job.save()	
			#  m2m must use save_m2m method if not immediatley commiting to db
			form.save_m2m()
			# new_objective.save()
			#  redirect to job detail page after submission
			return redirect('job_detail', job_details_id=new_job.pk)
		#  if a GET (or any other mehtod) blank form is created
	else:
		form = JobCreateForm(request = request) 
		# objective_form = ObjectiveCreateForm()

	context = {
		'form':form,
		# 'objective_form':objective_form,
		}
	return render(request, 'jobs/job_create.html', context)


@login_required
def objective_create(request, job_details_id):
	job_details = Job.objects.get(id=job_details_id)
	objectives = job_details.objectives.all()
	"""set objective within the project"""
	if request.method == 'POST':
		objective_form = ObjectiveCreateForm(request.POST)
		if objective_form.is_valid():
			new_objective = objective_form.save(commit=False)
			new_objective.job = job_details  # link objective to the the current job
			new_objective.save() 
			# return redirect('job_detail', job_details_id)
			return redirect('objective_create', job_details_id)
	else:
		objective_form = ObjectiveCreateForm()
		context = {
			'objective_form': objective_form,
			'objectives':objectives, 
			'job_details':job_details
		}

	return render(request, 'jobs/objective_create.html', context)

# #  adopted formset approach to allow for multiple additions of objectives 
# @login_required
# def objective_create(request, job_details_id):
# 	job_details = Job.objects.get(id=job_details_id)
# 	# ObjectiveFormSet = ObjectiveCreateFormSet()
# 	ObjectiveInlineFormSet= inlineformset_factory(
# 		Job,
# 		Objective,
# 		form=JobCreateForm,
# 		fields =('objective_description', 'objective_status', job_title),
# 		extra=0,
# 		can_delete = False
# 	)
# 	"""set objective within the project"""
# 	if request.method == 'POST':
# 		formset = ObjectiveInlineFormSet(request.POST, request.FILES, instance=job_details)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect('job_detail', job_details_id)
# 	else:
# 		#  GET
# 		formset = ObjectiveInlineFormSet(instance=job_details)
# 	return render(request, 'jobs/objective_create.html', {'formset': formset, })




def objective_detail(request, job_details_id, objective_id):
	"""objective detail page """
	#  job queryset
	job_details = Job.objects.get(id=job_details_id)
	objective = Objective.objects.get(id=objective_id)
	objective_comments = objective.objective_comments.all()
	if request.method == 'POST':
		form = ObjectiveCommentForm(request.POST)
		if form.is_valid():
			user_comment = form.save(commit=False)
			#  to link comment to the job through ForeignKey relationship 
			#  need to assign job model instance when saving comment model instance
			user_comment.objective = objective
			user_comment.comment_by = request.user
			user_comment.save()
			#  notify job author of comment 
			# notify_job_auth_comment(
			# 	user_comment.comment_by, 
			# 	job_details.author,
			# 	sender = user_comment.comment_by,
			# 	recipient = job_details.author,
			# 	verb = "commented",
			# 	target = job_details
			# 	)
			# #  notify personel associated to job when user comments
			# #  exclude commentor from recieving notification if he made the comment
			# personnel_list = job_details.personnel.exclude(id = request.user.id)
			# notify_job_personnel_comment(
			# 	sender = user_comment.comment_by,
			# 	recipient = personnel_list,
			# 	verb = "commented",
			# 	target = job_details
			# 	)
			return redirect ('objective_detail',job_details_id=job_details.id, objective_id=objective.id )
	else:
		form = ObjectiveCommentForm()
		paginator = Paginator(objective_comments, 15) # paginator 10 objects per view
		page = request.GET.get('page')  # paginator
		obj_pag = paginator.get_page(page)  # paginated object	
		context = {
			'obj_pag':obj_pag,
			'form':form,
			'job_details':job_details,
			'objective':objective,
			'objective_comments':objective_comments,
			
		}
	return render(request, 'jobs/objective_detail.html', context )



@login_required 
def job_update(request, job_id):
	""" Job update view form logic """
	job = Job.objects.get(id=job_id)
	job_title = job.job_title
	#  must be original author to update the job
	if job.author != request.user:
		raise Http404
	if request.method == "POST":
		form = JobCreateForm(request.POST, instance=job, request = request)
		if form.is_valid():
			update_job = form.save(commit=False)
			update_job.save()
			form.save_m2m()
			return redirect ('job_detail', job_details_id=update_job.pk)
	else: 
		#  pre-fill form with current entry
		form = JobCreateForm(instance=job, request = request)
	context = {
		'job':job,
		'job_title':job_title,
		'form':form
		}
	return render(request, 'jobs/job_update.html', context)


