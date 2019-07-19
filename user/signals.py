from django.db.models import post_save
from notification.signals import notify
from comments.model import Comment


def generate_notification(sender, instance, created, **kwargs):
	notify.send(instance, verb='commented')


post_save.connect(generate_notification, sender = Comment)