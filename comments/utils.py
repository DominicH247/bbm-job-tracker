from notifications.signals import notify

def notify_job_auth_comment(comment_by=None, author=None, **kwargs):
	"""send notification following comment save to job author"""
	# do not notify author if the job author makes a comment
	if comment_by != (author):
		notify.send(**kwargs)


def notify_job_personnel_comment(queryset=None,**kwargs):
	"""send notification to all personnel associated to job on user comment"""
	notify.send(**kwargs)