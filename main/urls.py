from django.urls import path
from .views import *


urlpatterns = [
    path('data_catalog', datacatalog_view, name='dataset_catalog'),
    path('data_catalog/dataset_detail/<int:pk>', dataset_detail_view, name='dataset_detail'),
    path('data_catalog/dataset_detail/<int:pk>/sample_data', dataset_sample_data, name='dataset_sample_data'),
]
