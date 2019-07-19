from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from tempus_dominus.widgets import DatePicker, DateTimePicker, TimePicker
from .models import Job, Objective
from user.models import CustomUser
from django.forms import inlineformset_factory


class JobCreateForm(forms.ModelForm):
	"""Create new job form"""
	def __init__(self, *args, **kwargs):
		"""over write form __init__ to include request"""
		self.request = kwargs.pop("request")
		super().__init__(*args, **kwargs)
		#  exlcue author (user.request) from appearing in personnel field
		self.fields["personnel"].queryset = CustomUser.objects.exclude(
			username = self.request.user
		)
		personnel = forms.ModelMultipleChoiceField(
			queryset = self.fields["personnel"].queryset,
			widget = forms.SelectMultiple(), 
			required=False
		)

	# close_date = forms.DateField(required=False, widget=AdminDateWidget(attrs={'placeholder':'Set closing date'}))
	deadline = forms.DateField(required=False, widget=AdminDateWidget(attrs={'placeholder':'Set deadline'}))

	class Meta:
		model = Job
		fields = [
			'job_title',
			'job_text',
			'personnel',
			'deadline',
			'job_status',
			# 'close_date',
		]


class ObjectiveCreateForm(forms.ModelForm):
	"""set objective on job creation"""
	class Meta: 
		model = Objective
		fields = [
			'objective_description',
			'objective_status',
		]


# ObjectiveCreateFormSet = inlineformset_factory(
# 	Job,
# 	Objective,
# 	# form=JobCreateForm,
# 	fields =('objective_description', 'objective_status'),
# 	extra=1,
# 	can_delete = False
# 	)

	









