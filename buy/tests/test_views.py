from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from buy.models import Listing, Comment
from decimal import Decimal

class ViewTestCase(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Create test listing
        self.listing = Listing.objects.create(
            title="Test Listing",
            slug="test-listing",
            author=self.user,
            manufacturer="Rolex",
            body="Test Body",
            price=Decimal('999.99'),
            status=1
        )

    def test_ListingsList_view(self):
        response = self.client.get(reverse('buy:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Listing")
        self.assertTemplateUsed(response, 'buy/index.html')
    
    def test_watch_detail_view(self):
        url = reverse('buy:watch_detail', args=[self.listing.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Listing")
        self.assertTemplateUsed(response, 'buy/watch_detail.html')

    # Continue with tests for like_listing, add_comment_to_listing, delete_comment, and place_bid
