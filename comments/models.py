from django.db import models
from jobs.models import Job, Objective
from django.conf import settings
from django.utils import timezone
from user.models import CustomUser
# Create your models here.
class Comment(models.Model):
	"""User comment model"""
	job = models.ForeignKey(
		Job,
		null = True,
		on_delete=models.CASCADE,
		related_name = 'comments'
	)
	text = models.TextField()
	comment_date = models.DateTimeField(auto_now_add=True)
	comment_by = models.ForeignKey(
		CustomUser, 
		on_delete=models.CASCADE,
		) 

	class Meta:
		ordering = ('-comment_date',)

	def __str__(self):
		return self.text


class ObjectiveComment(models.Model):
	"""User Objective comments model"""
	objective = models.ForeignKey(
		Objective,
		null = True,
		on_delete=models.CASCADE,
		related_name = 'objective_comments'
	)
	text = models.TextField()
	comment_date = models.DateTimeField(auto_now_add=True)
	comment_by = models.ForeignKey(
		CustomUser, 
		on_delete=models.CASCADE,
		) 

	class Meta:
		ordering = ('-comment_date',)

	def __str__(self):
		return self.text


	