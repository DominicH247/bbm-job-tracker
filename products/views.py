from django.shortcuts import render
from django.views.generic import ListView

from .models import PharmaProduct

class ProductListView(ListView):
	model = PharmaProduct
	context_object_name = 'product_list'
	template_name = 'products/product_list.html'

	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super().get_context_data(**kwargs)
	    # get product count
	    context['product_count'] = PharmaProduct.objects.count()
	    return context

