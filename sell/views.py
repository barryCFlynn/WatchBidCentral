from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateListing
from buy.models import Listing, ListingImage

@login_required
def create_listing(request, slug=None):
    listing = None
    if slug:
        listing = get_object_or_404(Listing, slug=slug, author=request.user)  # Ensure the user is the author
        form = CreateListing(request.POST or None, request.FILES or None, instance=listing)
    else:
        form = CreateListing(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        listing = form.save(commit=False)
        listing.author = request.user  # Set the author to the current user
        listing.save()

        # Handle image uploads
        images = request.FILES.getlist('images')  # Get uploaded images
        if images:
            ListingImage.objects.filter(listing=listing).delete()  # Optional: Remove existing images
            for image_file in images:
                ListingImage.objects.create(listing=listing, image=image_file)

        messages.success(request, 'Listing saved successfully!')
        return redirect('watch_detail', slug=listing.slug)

    return render(request, 'sell/create_listing.html', {'form': form, 'listing': listing})

@login_required
def my_listings(request):
    # Query listings by the current logged-in user
    listings = Listing.objects.filter(author=request.user).order_by('-created_on')  # Adjust 'date_posted' accordingly
    return render(request, 'sell/my_listings.html', {'listings': listings})

@login_required
def delete_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    
    if listing.author != request.user:
        messages.error(request, "You do not have permission to delete this listing.")
        return redirect('watch_detail', listing.slug)
    
    if request.method == 'POST':
        listing.delete()
        messages.success(request, "Your listing was successfully deleted.")
        return redirect('my-listings')
    else:
        return redirect('watch_detail', listing.slug)