from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Listing


# Create your views here.
class ListingsList(generic.ListView):
    queryset = Listing.objects.filter(status=1) #Filter out "draft" listing status=0
    template_name = "buy/index.html"
    ordering = ['-created_on']  # Ordering by created_on field in descending order
    # TODO remove paginate once implement single page 
    # scrolling through inventory
    # paginate_by = 8

#TODO fix this, it is not grabbing the iformation
class top_listings_carousel(generic.ListView):
    def get(self, request, *args, **kwargs):
        print("View function top_listings_carousel is being called")
        return super().get(request, *args, **kwargs)

    queryset = Listing.objects.filter(status=1)
    template_name = "buy/index.html"
    ordering = ('-likes')[:10]

def watch_detail(request, slug):
    """
    Display an individual :model:`buy.Listing`.

    **Context**

    ``listing``
        An instance of :model:`buy.Listing`.

    **Template:**

    :template:`buy/watch_detail.html`
    """

    queryset = Listing.objects.filter(status=1)
    watch = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "buy/watch_detail.html",
        {"watch": watch},
    )