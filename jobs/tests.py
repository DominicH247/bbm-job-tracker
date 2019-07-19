from django.test import SimpleTestCase, TestCase
from django.test.client import Client
from .views import job_detail
from .models import Job
from user.models import CustomUser
from django.urls import reverse


class SetupClass(TestCase):
	"""generate testuser for the test client"""
	def setUp(self):
		self.user =  CustomUser.objects.create_user(
			'testuser1',
			'test@email.com',
			'testpassword1'
		)
		self.client = Client()
		self.client.login(username = 'testuser1', password = 'testpassword1')

class JobViewsTest(SetupClass):
	""" Test if Job views return the correct views 
	and templates """
	def test_job_list_view(self):
		response = self.client.get(reverse('job_list'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'jobs/job_list.html')

	def test_job_detail_view(self):
		job_detail = Job.objects.create()
		response = self.client.get(reverse('job_detail', args=[job_detail.id]))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'jobs/job_detail.html')

	def test_job_list_open(self):
		response = self.client.get(reverse('job_list_open'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'jobs/job_list_open.html')

	def test_job_list_closed(self):
		response = self.client.get(reverse('job_list_closed'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'jobs/job_list_closed.html')

	def test_job_create(self):
		response = self.client.get(reverse('job_create'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'jobs/job_create.html')

	def test_job_update(self):
		"""View contains if job.author != request.user"""
		#  create job object with self,user instance as author
		job = Job.objects.create(author = self.user)
		response = self.client.get(reverse('job_update', args=[job.id]))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'jobs/job_update.html')

