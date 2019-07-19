from django.urls import path, include
from django.views.i18n import JavaScriptCatalog


from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_details_id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_details_id>/objective/<int:objective_id>/', views.objective_detail, name='objective_detail'),
    path('job_open/', views.job_list_open, name = 'job_list_open'),
    path('job_closed/', views.job_list_closed, name = 'job_list_closed'),
    path('job/create/', views.job_create, name='job_create'),
    path('job/<int:job_details_id>/create_objective/', views.objective_create, name='objective_create'),
    path('job/<int:job_id>/update', views.job_update, name = 'job_update'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),  # uses admin form styling
]
