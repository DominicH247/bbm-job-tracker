from django.shortcuts import render
from django.views.generic import ListView

from .models import Variation

class VariationListView(ListView):
	"""List of all variations"""
	model = Variation
	context_object_name = 'variation_list'
	template_name = 'variationtracker/variation_list.html'

	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super().get_context_data(**kwargs)
	    # get product count
	    context['variation_count'] = Variation.objects.count()
	    return context
