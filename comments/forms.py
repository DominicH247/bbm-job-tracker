from django import forms
from .models import Comment, ObjectiveComment

class UserCommentForm(forms.ModelForm):
	"""user comment form"""
	#  overwtire form field to change label
	text = forms.CharField(label='Comment', widget=forms.Textarea)
	class Meta:
		model = Comment
		fields = [
			'text',
		]


class ObjectiveCommentForm(forms.ModelForm):
	"""user objective comment form"""
	#  overwtire form field to change label
	text = forms.CharField(label='Comment', widget=forms.Textarea)
	class Meta:
		model = ObjectiveComment
		fields = [
			'text',
		]