from django.urls import path
from .views import index, otu_table

urlpatterns = [
    path('', index, name='index'),
    path('otu_table/', otu_table, name='otu_table'),
]