from django.shortcuts import render
from django.views import generic
from .models import Listing


# Create your views here.
class Listings(generic.ListView):
    model = Listing