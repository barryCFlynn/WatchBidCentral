from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.urls import reverse
from .models import Listing, Comment


# Create your views here.
class ListingsList(ListView):
    model = Listing
    template_name = "buy/index.html"
    context_object_name = 'listing_list'  # This will be used to access the listings in the template
    queryset = Listing.objects.filter(status=1).order_by('-created_on')  # Adjusted for clarity

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the top 7 most liked listings
        context['like_listings'] = Listing.objects.order_by('-likes')[:7]
        return context


def watch_detail(request, slug):
    """
    Display an individual :model:`buy.Listing`.

    **Context**

    ``watch``
        An instance of :model:`buy.Listing`.

    **Template:**

    :template:`buy/watch_detail.html`
    """
    listing = get_object_or_404(Listing, slug=slug)
    return render(request, 'buy/watch_detail.html', {'listing': listing})

# def like_carousel(request):
#     # Fetch the top 7 most liked listings
#     like_listings = Listing.objects.order_by('-likes')[:7]
#     context = {
#         'like_listings': like_listings,
#     }
#     return render(request, 'index.html', context)

def like_listing(request, listing_id):
    # Ensure this action only happens for authenticated users
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)

    listing = get_object_or_404(Listing, id=listing_id)
    listing.likes += 1
    listing.save()
    return JsonResponse({'likes': listing.likes})

@login_required
def add_comment_to_listing(request, slug):
    listing = get_object_or_404(Listing, slug=slug)
    if request.method == "POST":
        comment_body = request.POST.get('comment')
        comment = Comment(listing=listing, author=request.user, body=comment_body)
        comment.save()
        return redirect('watch_detail', slug=slug)
    else:
        # Optionally handle the case for GET request or show an error
        return redirect('watch_detail', slug=listing.slug)
