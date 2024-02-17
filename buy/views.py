from django.shortcuts import render
from django.views import generic
from .models import Listing


# Create your views here.
class Listings(generic.ListView):
    queryset = Listing.objects.filter(status=1)
    template_name = "buy/index.html"
    paginate_by = 6