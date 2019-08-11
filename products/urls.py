from django.urls import path, include


from .views import ProductListView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
]
