from notifications.signals import notify


class UserNotification: 
	"""User notification class"""
	def __init__(self, personnel_list=None, recipient=None, author=None, sender=None, **kwargs):
		self.kwargs = kwargs
		self.recipient = recipient
		self.personnel_list = personnel_list
		self.author = author
		self.sender = sender

	def send_notification_author(self):
		"""send notification to author when user comments on post"""
		if self.sender != (self.author):
			notify.send(recipient=self.recipient, sender=self.sender, **self.kwargs)

	def send_notification_personnel(self):
		"""send notification to all personnel associated with the job"""
		notify.send(recipient=self.personnel_list, sender=self.sender, **self.kwargs)