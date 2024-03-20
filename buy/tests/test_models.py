from django.test import TestCase
from django.contrib.auth.models import User
from buy.models import Listing, ListingImage, Comment
from decimal import Decimal
from cloudinary.models import CloudinaryField

class ListingModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user for the author field
        cls.user = User.objects.create_user(username='testuser', password='12345')

        # Create a listing with minimum required information
        Listing.objects.create(
            title='Test Listing',
            author=cls.user,
            manufacturer='Rolex',
            body='Description of the listing.',
            price='1000.00',
            current_bid='1050.00',
            reserve='1500.00'
        )

    def test_listing_slug_on_save(self):
        """Test the slug is automatically generated if not provided."""
        listing = Listing.objects.get(id=1)
        self.assertIsNotNone(listing.slug, "Slug should not be None after saving.")
        self.assertEqual(listing.slug, 'test-listing', "Slug does not match expected value.")

    def test_listing_str_method(self):
        """Test the string representation of Listing model."""
        listing = Listing.objects.get(id=1)
        expected_object_name = f"The title of this listing is {listing.title} | written by {listing.author}"
        self.assertEqual(str(listing), expected_object_name)

    def test_listing_has_correct_manufacturer(self):
        """Test listing manufacturer is saved correctly."""
        listing = Listing.objects.get(id=1)
        self.assertEqual(listing.manufacturer, 'Rolex', "Manufacturer does not match.")

    def test_listing_price(self):
        """Test listing price is saved correctly."""
        listing = Listing.objects.get(id=1)
        self.assertEqual(listing.price, Decimal('1000.00'), "Price does not match expected value.")


class ListingImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a User
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()
        
        # Create a Listing
        test_listing = Listing.objects.create(
            title='Test Listing',
            status=1,
            slug='test-listing',
            author=test_user,
            manufacturer='Rolex',
            body='Test listing body.',
            price=1000.00
        )
        test_listing.save()
        
        # Create a ListingImage
        test_image = ListingImage.objects.create(
            listing=test_listing,
            image='image_url'  # Assuming 'image_url' is a valid Cloudinary URL for testing
        )
        test_image.save()

    def test_listing_image_str(self):
        image = ListingImage.objects.get(id=1)
        expected_object_name = f'{image.listing.title} Image'
        self.assertEqual(str(image), expected_object_name)


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()

        # Create a listing
        test_listing = Listing.objects.create(
            title='Test Listing',
            slug='test-listing',
            author=test_user,
            manufacturer='Rolex',
            body='Test listing body',
            price=1000.00
        )
        test_listing.save()

        # Create a comment
        test_comment = Comment.objects.create(
            listing=test_listing,
            author=test_user,
            body='Test comment body'
        )
        test_comment.save()

    def test_comment_content(self):
        comment = Comment.objects.get(id=1)
        expected_author_username = comment.author.username
        expected_listing_title = comment.listing.title
        expected_body = comment.body
        self.assertEqual(expected_author_username, 'testuser')
        self.assertEqual(expected_listing_title, 'Test Listing')
        self.assertEqual(expected_body, 'Test comment body')

    def test_comment_string_representation(self):
        comment = Comment.objects.get(id=1)
        expected_string = f"Comment by {comment.author}: {comment.body[:30]}{'...' if len(comment.body) > 30 else ''}"
        self.assertEqual(str(comment), expected_string)
