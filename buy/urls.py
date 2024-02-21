from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListingsList.as_view(), name='home'),
    path('<slug:slug>/', views.watch_detail, name='watch_detail'),
]