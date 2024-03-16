from . import views
from django.urls import path

urlpatterns = [
    path('create-listing/', views.create_listing, name='create-listing'),
    path('my-listings/', views.my_listings, name='my-listings'),
]