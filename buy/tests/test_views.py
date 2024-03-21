from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from buy.models import Listing, Comment
from decimal import Decimal

class BuyViewTestCase(TestCase):
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
            price=Decimal('1000.00'),
            current_bid=Decimal('1050.00'),
            status=1
        )

        # Create test comment
        self.comment = Comment.objects.create(
            listing=self.listing,
            author=self.user,
            body="This is a sample comment."
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

    def test_like_listing_authenticated_user(self):
        # Test that an authenticated user can like a listing and likes are incremented
        initial_likes = self.listing.likes
        response = self.client.post(reverse('buy:like_listing', args=[self.listing.id]))
        self.listing.refresh_from_db()  # Refresh the listing object from the database
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.listing.likes, initial_likes + 1)
        self.assertJSONEqual(response.content.decode(), {'likes': self.listing.likes})

    def test_like_listing_unauthenticated_user(self):
        # Test that an unauthenticated user cannot like a listing
        self.client.logout()  # Log out to simulate an unauthenticated user
        response = self.client.post(reverse('buy:like_listing', args=[self.listing.id]))
        
        self.assertEqual(response.status_code, 401)
        self.assertJSONEqual(response.content.decode(), {'error': 'Authentication required'})

    def test_place_bid_successful(self):
        self.client.login(username='testuser', password='12345')
        new_bid_amount = Decimal('1100.00')
        response = self.client.post(reverse('buy:place_bid', args=[self.listing.id]), {'bid_amount': new_bid_amount})
        
        self.listing.refresh_from_db()
        self.assertEqual(self.listing.current_bid, new_bid_amount)
        
        # Check if a comment noting the bid was created
        comment_text = f"Bid placed: € {new_bid_amount:,.2f}"
        self.assertTrue(Comment.objects.filter(body__contains=comment_text).exists())
        
        # Ensure the response is a redirection to the watch detail view of the listing
        self.assertRedirects(response, reverse('buy:watch_detail', kwargs={'slug': self.listing.slug}))

    