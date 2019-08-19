from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

from .views import VariationListView, VariationDetailView, VariationCreateView

urlpatterns = [
    path('list/', VariationListView.as_view(), name='variation_list'),
    path('<int:pk>/', VariationDetailView.as_view(), name='variation_detail'),
    path('create/', VariationCreateView.as_view(), name='variation_create'),
    path('jsi18n/', JavaScriptCatalog.as_view(),
         name='javascript-catalog'),  # uses admin form styling
]
