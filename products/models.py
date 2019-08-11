from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class PharmaProduct(models.Model):
	"""Braun Pharmaceutical products"""
	product_name = models.CharField(max_length = 100)
	solution_number = models.CharField(max_length = 10)
	# prevent white spaces in filed
	licence_number = models.CharField(max_length = 9, validators=[RegexValidator(
		regex='^[^\s]+$',
		message='No spaces allowed',
		code = 'invalid_licence_number'
		),])
	licence_holder = models.CharField(max_length = 100)
	# storage_conditions = models.CharField(max_length = 100)
	NATIONAL = 'National'
	MRP_DCP = 'MRP/DCP'
	CENTRALISED = 'Centralised'
	PROCEDURE_TYPE_CHOICES = (
		(NATIONAL, 'National'),
		(MRP_DCP, 'MRP/DCP'),
		(CENTRALISED, 'Centralised')
	)
	procedure_type = models.CharField(
		choices = PROCEDURE_TYPE_CHOICES,
		max_length = 12,
		default = NATIONAL
		)


	def __str__ (self):
		return self.product_name

	def format_licencenumber(self):
		"""format licence number"""
		f1 = self.licence_number[0:5]
		f2 = self.licence_number[5:9]
		formatted_ln = "PL-"+f1+"-"+f2
		return formatted_ln


	def save(self, *args, **kwargs):
		"""convert product_name to lower case"""
		self.product_name = self.product_name.lower()
		self.licence_number = self.format_licencenumber()
		return super(PharmaProduct, self).save(*args, **kwargs)
