from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListingsList.as_view(), name='home'),
    path('<slug:slug>/', views.watch_detail, name='watch_detail'),
    # Add the new URL pattern for the like functionality
    path('like_listing/<int:listing_id>/', views.like_listing, name='like_listing'),
]