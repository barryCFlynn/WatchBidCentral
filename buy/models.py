from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta
from django.contrib.auth.models import User
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
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # image_1 = CloudinaryField('image_1', default='placeholder')
    # image_2 = CloudinaryField('image_2', default='placeholder')
    # image_3 = CloudinaryField('image_3', default='placeholder')
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
    price = price = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reserve = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"The title of this post is {self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores single comment entry related to :model:`auth.User`,
    :model:`buy.Listing` and :model:`buy.Comment` .
    """
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True) 
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"