from django.urls import path, include

from .views import VariationListView, VariationDetailView

urlpatterns = [
    path('list/', VariationListView.as_view(), name='variation_list'),
    path('<int:pk>/', VariationDetailView.as_view(), name='variation_detail')
    
]
