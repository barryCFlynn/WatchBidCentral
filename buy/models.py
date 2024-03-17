from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import timedelta
from cloudinary.models import CloudinaryField

# from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1,"Listed"))

# Create your models here.

class Listing(models.Model):
    """
    Store a single buy listing entry related to :model:`auth.User`.
    """
    MANUFACTURER_CHOICES = [
        ('Audemars Piguet', 'Audemars Piguet'),
        ('Blancpain', 'Blancpain'),
        ('Breguet', 'Breguet'),
        ('Breitling', 'Breitling'),
        ('Bulgari', 'Bulgari'),
        ('Cartier', 'Cartier'),
        ('Casio', 'Casio'),
        ('Chopard', 'Chopard'),
        ('Citizen', 'Citizen'),
        ('Fossil', 'Fossil'),
        ('Girard-Perregaux', 'Girard-Perregaux'),
        ('Hamilton', 'Hamilton'),
        ('Hublot', 'Hublot'),
        ('IWC Schaffhausen', 'IWC Schaffhausen'),
        ('Jaeger-LeCoultre', 'Jaeger-LeCoultre'),
        ('Longines', 'Longines'),
        ('Montblanc', 'Montblanc'),
        ('Omega', 'Omega'),
        ('Oris', 'Oris'),
        ('Panerai', 'Panerai'),
        ('Patek Philippe', 'Patek Philippe'),
        ('Piaget', 'Piaget'),
        ('Rado', 'Rado'),
        ('Raymond Weil', 'Raymond Weil'),
        ('Rolex', 'Rolex'),
        ('Seiko', 'Seiko'),
        ('TAG Heuer', 'TAG Heuer'),
        ('Tissot', 'Tissot'),
        ('Tudor', 'Tudor'),
        ('Ulysse Nardin', 'Ulysse Nardin'),
        ('Vacheron Constantin', 'Vacheron Constantin'),
        ('Zenith', 'Zenith')
        # Add more choices as needed
    ]
    title = models.CharField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=1)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_listings"
    )
    manufacturer = models.CharField(max_length=100, choices=MANUFACTURER_CHOICES, default='None Selected')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    bid_timer = models.DurationField(
        verbose_name='Bid Timer',
        default=timedelta(days=30),
        validators=[
            MinValueValidator(limit_value=timedelta(days=1)),
            MaxValueValidator(limit_value=timedelta(days=60))
        ],
        null=True,
        blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reserve = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:  # Check if the slug needs to be generated
            # Generate slug ensuring uniqueness using a UUID
            self.slug = slugify(self.title)[:180]  # Trim slug size to fit max_length if necessary
            unique_slug = self.slug
            num = 1
            while Listing.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(self.slug, num)
                num += 1
            self.slug = unique_slug

        super(Listing, self).save(*args, **kwargs)


    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"The title of this listing is {self.title} | written by {self.author}"

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f"{self.listing.title} Image"

class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User` and :model:`buy.Listing`.
    Supports nested comments through the 'parent_comment' field.
    """
    listing = models.ForeignKey(
        Listing, 
        on_delete=models.CASCADE, 
        related_name="comments"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name="user_comments"
    )
    parent_comment = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name="replies"  # Helps in querying child comments of a parent
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        # Truncate body in string representation for readability
        return f"Comment by {self.author}: {self.body[:30]}{'...' if len(self.body) > 30 else ''}"
