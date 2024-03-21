from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from buy.models import Listing, ListingImage
from decimal import Decimal

class SellViewsTestCase(TestCase):
    def setUp(self):
        # Create a user for the tests
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
        # Create a test listing
        self.listing = Listing.objects.create(
            title="Test Listing",
            slug="test-listing",
            author=self.user,
            manufacturer="Test Manufacturer",
            body="Test description",
            price=Decimal("100.00")
        )
    
    def test_create_listing_get(self):
        # Test the create listing page loads correctly
        response = self.client.get(reverse('sell:create-listing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sell/create_listing.html')
    
    def test_my_listings(self):
        # Test the my listings view
        response = self.client.get(reverse('sell:my-listings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sell/my_listings.html')
        self.assertContains(response, "Test Listing")  # Check if the listing appears in the template

    def test_delete_listing(self):
        # Test the delete listing view
        response = self.client.post(reverse('sell:listing-delete', args=[self.listing.id]))
        self.assertEqual(Listing.objects.count(), 0)  # Assuming the listing was deleted
        self.assertRedirects(response, reverse('sell:my-listings'))


# Adjust the reverse URLs (e.g., 'sell:create-listing', 'sell:my-listings', 'sell:delete-listing') to match your project's URL names.
