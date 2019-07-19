from django.conf import settings
from django.db import models
from django.utils import timezone
from user.models import CustomUser

class Job(models.Model):
	"""A model for active jobs"""
	job_title = models.CharField(max_length=200)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		null=True, 
		on_delete=models.SET_NULL, 
		related_name = 'authors'
		)  # do not want to delete all posts when user is deleted
	# many to many as job can have many personnel assigned to it 
	# and personnel can be assigned to many jobs.
	personnel = models.ManyToManyField(CustomUser, blank=True)
	job_text = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)  # auto time stamp on object creation =True allows modification 
	last_update = models.DateTimeField(null=True, auto_now=True)  # auto add time stamp when object modified, can not be edited
	deadline = models.DateField(null=True, blank=True)
	#  Job status choices 
	OPEN = 'Open'
	CLOSED = 'Closed'
	JOB_STATUS_CHOICES = (
		(OPEN, 'Open'),
		(CLOSED, 'Closed')
	)
	job_status = models.CharField(
		choices = JOB_STATUS_CHOICES,
		max_length = 15,
		null = True,
		blank = True,
		default = ''
	)
	close_date = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.job_title


class Objective(models.Model):
	""" objectives model linked to job"""
	job = models.ForeignKey(
		Job, 
		null=True, 
		on_delete=models.CASCADE,
		related_name = 'objectives' )
	objective_description = models.CharField(max_length = 200)
	created_date = models.DateTimeField(null=True, auto_now=True)
	last_update = models.DateTimeField(null=True, auto_now=True)
	completion_date = models.DateTimeField(null=True, blank=True)
	#  objective status choices 
	TO_START = 'To Start'
	IN_PROGRESS = 'In Progress'
	COMPLETE = 'Complete'
	OBSOLETE = 'Obsolete'
	OBJECTIVE_STATUS_CHOICES = (
		(TO_START, 'To Start'),
		(IN_PROGRESS, 'In Progress'),
		(COMPLETE, 'Complete'),
		(OBSOLETE, 'Obsolete'),
	)
	objective_status = models.CharField(
		choices = OBJECTIVE_STATUS_CHOICES,
		max_length = 15,
		null = True,
		blank = True,
		default = ''
	)

	def __str__(self):
		return self.objective_description

