from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CreateListing

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
            return redirect(reverse('buy/watch_detail.html', args=[listing.slug]))
    else:
        form = CreateListing()
    return render(request, 'sell/create_listing.html', {'form': form})