from django.db import models
from products.models import PharmaProduct
from user.models import CustomUser

class Variation(models.Model):
	"""Variation model"""
	# automatically assign reference
	lra_reference = models.CharField(max_length = 100)
	product = models.ForeignKey(
		PharmaProduct, 
		on_delete=models.CASCADE,
		null = True,
		related_name = 'products'
		)
	procedure_number = models.CharField(max_length = 50)
	variation_description = models.TextField()
	date_recieived = models.DateField(auto_now_add=True) # can be edited
	owner = models.ForeignKey(
		CustomUser,
		on_delete = models.CASCADE,
		null = True,
		related_name = 'owners'
		)
	personnel = models.ManyToManyField(CustomUser, blank=True)
	date_pre_submission = models.DateField(null=True, blank=True)
	date_submission = models.DateField(null=True, blank=True)
	date_approval = models.DateField(null=True, blank=True)
	date_internal_approval_completion = models.DateField(null=True, blank=True)
	date_variation_closed = models.DateField(null=True, blank=True)

	# Variation status choices
	OPEN = 'Open'
	CLOSED = 'Closed'
	VARIATION_STATUS_CHOICES = (
		(OPEN, 'Open'),
		(CLOSED, 'Closed')
	)
	variation_status = models.CharField(
		choices = VARIATION_STATUS_CHOICES,
		max_length = 15,
		null = True,
		blank = True,
		default = ''
	)	
	# Raised by choices
	LRA = 'LRA'
	GRA = 'GRA'
	MHRA = 'MHRA'
	OTHER = 'Other'
	RAISED_BY_CHOICES = (
		(LRA, 'LRA'),
		(GRA, 'GRA'),
		(MHRA, 'MHRA'),
		(OTHER, 'Other')
	)
	initiated_by = models.CharField(
		choices = RAISED_BY_CHOICES,
		max_length = 10,
		null = True,
		blank = True,
		default = ''
	)		
	# Outcome
	APPROVED = 'Approved'
	RFI = 'RFI'
	REJECTED = 'Rejected' 
	OUTCOME_CHOICES = (
		(APPROVED, 'Approved'),
		(RFI, 'RFI'),
		(REJECTED, 'Rejected'),
	)
	# Variation Type
	IAN = 'IAN'
	IA = 'IA'
	IIB = 'IB'
	II = 'II'
	VARIATION_TYPE_CHOICES = (
		(IAN, 'IAN'),
		(IA, 'IA'),
		(IIB, 'IB'),
		(II , 'II')
	)
	variation_type = models.CharField(
		choices = VARIATION_TYPE_CHOICES,
		max_length = 10,
		null = True,
		blank = True,
		default = ''
	)	
	# Variation Reason
	QUALITY = 'Quality'
	PI = 'Patient Information'
	VARIATION_REASON_CHOICES = (
		(QUALITY, 'Quality'),
		(PI, 'Patient Information')
	)
	variation_reason = models.CharField(
		choices = VARIATION_REASON_CHOICES,
		max_length = 20,
		null = True,
		blank = True,
		default = ''
	)		

	def autoset_close_date(self):
		"""set closing date automatically when status set to CLOSED """
		if VARIATION_STATUS_CHOICES == CLOSED:
			date_variation_closed =  models.DateField(auto_now_add=True)


class Dossier(models.Model):
	"""documents required for pressubmission"""
	variation = models.ForeignKey(
		Variation,
		on_delete=models.CASCADE,
		null = True,
		related_name = 'dossier_variations'
		)
	# Cover letter, SmPC, PIL, Labels, mock-ups (PIL), mock-ups (labels)
	document_type = models.CharField(max_length = 100)
	date_completed = models.DateField(null=True, blank=True)
	date_submitted = models.DateField(null=True, blank=True)


class ReSubmission(models.Model):
	"""resubmission of documents if required"""
	variation = models.ForeignKey(
		Variation,
		on_delete=models.CASCADE,
		null = True,
		related_name = 'resubmission_variations'
		)
	reason = models.TextField()
	documents_required = models.ForeignKey(
		Dossier,
		on_delete=models.CASCADE,
		null = True,
		related_name= 'resubmission_dossiers'
		)
	date_resubmitted = models.DateField(null=True, blank=True)


class InternalApproval(models.Model):
	"""internal approval class"""
	variation = models.ForeignKey(
		Variation,
		on_delete=models.CASCADE,
		null = True,
		related_name = 'internalapproval_variations'
		)
	finalised_documents = models.ForeignKey(
		Dossier,
		on_delete=models.CASCADE,
		null = True,
		related_name= 'internalapproval_dossiers'
		)
	date_workflow_init = models.DateField(null=True, blank=True)
	date_workflow_approved = models.DateField(null=True, blank=True)


class NationalPhase(models.Model):
	"""national phase class"""
	variation = models.ForeignKey(
		Variation,
		on_delete=models.CASCADE,
		null = True,
		related_name = 'nationalphase_variations'
		)
	finalised_documents = models.ForeignKey(
		Dossier,
		on_delete=models.CASCADE,
		null = True,
		related_name= 'nationalphase_dossiers'
		)
	date_submission = models.DateField(null=True, blank=True)
		#  national phase requirement choices
	YES= 'Yes'
	NO = 'N/A'
	NATIONALPHASE_REQUIERMENT_CHOICES = (
		(YES, 'Yes'),
		(NO, 'N/A'),
	)		

