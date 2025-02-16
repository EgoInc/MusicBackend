# merch/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('merch/', views.MerchListView.as_view(), name='merch-list'),
    path('merch/<int:merch_id>/', views.MerchDetailView.as_view(), name='merch-detail'),
]
