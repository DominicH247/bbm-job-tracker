from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Variation
from products.models import PharmaProduct

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

class VariationDetailView(DetailView):
	"""detail view of variation"""
	model = model = Variation
	context_object_name = 'variation_detail'
	template_name = 'variationtracker/variation_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		variation = self.get_object()
		context['product_list'] = variation.product
		return context


