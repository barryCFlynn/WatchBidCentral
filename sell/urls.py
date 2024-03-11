from . import views
from django.urls import path

urlpatterns = [
    path('create-listing/', views.create_listing, name='create-listing'),
]