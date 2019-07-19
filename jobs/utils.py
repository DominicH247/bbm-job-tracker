from datetime import date 
from jobs.models import Job

class Deadline:
	"""Class to retreive job deadlines"""
	def __init__(self, job_id):
		self.job_id = job_id
		# self.job_deadline = job_deadline	

	def check_deadline(self):
		"""Check if job is overdue"""
		current_date = date.today()
		job_deadline = self.job_id.deadline
		difference = job_deadline - current_date
		#  return output in days
		days_left = difference.days
		#  check if current date is over deadline
		if current_date > job_deadline:
			message_over = ("You are {0} days overdue!".format(days_left))
			return message_over
		else: 
			message_under = ("You have {0} days until the deadline.".format(days_left))
			return message_under




