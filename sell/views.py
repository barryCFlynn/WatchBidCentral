from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateListing
from buy.models import Listing

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = CreateListing(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = request.user  # Set the author to the current user
            listing.save()
            # Add a success message
            messages.success(request, 'Your listing was created successfully!')
            # Redirect to the watch_detail view of the new listing
            return redirect(reverse('watch_detail', args=[listing.slug]))
    else:
        form = CreateListing()
    return render(request, 'sell/create_listing.html', {'form': form})

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