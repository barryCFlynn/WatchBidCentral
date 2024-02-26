from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import generic
from django.views.decorators.http import require_GET
from django.urls import reverse
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
        return super().get(request, *args, **kwargs)

    queryset = Listing.objects.filter(status=1)
    template_name = "buy/index.html"
    ordering = ('-likes')[:10]

def watch_detail(request, slug):
    """
    Display an individual :model:`buy.Listing`.

    **Context**

    ``watch``
        An instance of :model:`buy.Listing`.

    **Template:**

    :template:`buy/watch_detail.html`
    """

    # Retrieve the Listing object with the specified slug or return a 404 error if not found
    watch = get_object_or_404(Listing, slug=slug, status=1)  # Filter by status=1 to only get active listings

    # Pass the watch object to the template context and render the template
    return render(
        request,
        "buy/watch_detail.html",
        {"watch": watch},  # Pass the watch object as context data
    )

def like_listing(request, listing_id):
    # Ensure this action only happens for authenticated users
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)

    listing = get_object_or_404(Listing, id=listing_id)
    listing.likes += 1
    listing.save()
    return JsonResponse({'likes': listing.likes})

def add_comment_to_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.method == "POST":
        comment_body = request.POST.get('comment')
        comment = Comment(listing=listing, author=request.user, body=comment_body)
        comment.save()
        return HttpResponseRedirect(reverse('watch_detail', args=[listing.slug]))
    # Redirect or show an error if not POST request or other conditions are not met