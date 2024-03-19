from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListingsList.as_view(), name='home'),
    path('listing/<slug:slug>/', views.watch_detail, name='watch_detail'),
    path('like_listing/<int:listing_id>/', views.like_listing, name='like_listing'),
    path('listing/<slug:slug>/add_comment/', views.add_comment_to_listing, name='add_comment_to_listing'),
    path('listing/<int:listing_id>/place_bid/', views.place_bid, name='place_bid'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]