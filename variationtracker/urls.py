from django.urls import path, include

from . import views

urlpatterns = [
    path('variationtracker/variations', VariationListView.as_View(), name='variation_list'),
    
]
